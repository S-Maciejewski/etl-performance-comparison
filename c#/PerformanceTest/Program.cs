using System;
using System.IO.Compression;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using System.Threading.Tasks.Dataflow;

namespace PerformanceTest
{
    class Program
    {
        static void Main(string[] args)
        {
            var testFiles = Directory.GetFiles("../../test_data");

            var downloadBlock = new TransformBlock<string, MemoryStream>(url =>
            {
                // Download file (async) and pass FileStream to unzipBlock
                MemoryStream memoryStream = new MemoryStream();

                using (FileStream fileStream = File.OpenRead(url))
                {
                    memoryStream.SetLength(fileStream.Length);
                    fileStream.Read(memoryStream.GetBuffer(), 0, (int)fileStream.Length);
                }

                return memoryStream;
            },
            new ExecutionDataflowBlockOptions
            {
                MaxDegreeOfParallelism = 2, // How many files do we want to download at once? How good is download speed / bandwith?
            });

            var unzipBlock = new ActionBlock<MemoryStream>(async memoryStream =>
            {
                ZipArchive zipArchive = new ZipArchive(memoryStream);
                MemoryStream outputStream = new MemoryStream();

                await Task.Run(() =>
                {
                    foreach (ZipArchiveEntry entry in zipArchive.Entries)
                    {
                        // Load results to database
                        entry.Open().CopyTo(outputStream);
						Encoding.ASCII.GetString(outputStream.ToArray());
                        // Console.WriteLine(Encoding.ASCII.GetString(outputStream.ToArray()));
                    }
                });
            },
            new ExecutionDataflowBlockOptions
            {
                BoundedCapacity = Environment.ProcessorCount * 3,
                MaxDegreeOfParallelism = Environment.ProcessorCount,
            });

            downloadBlock.LinkTo(
            unzipBlock,
            new DataflowLinkOptions
            {
                PropagateCompletion = true,
            });


			// Measure performance
			var watch = System.Diagnostics.Stopwatch.StartNew();

            foreach (var url in testFiles)
            {
                downloadBlock.Post(url);
            }
            downloadBlock.Complete();
            unzipBlock.Completion.GetAwaiter().GetResult();

			watch.Stop();
			Console.WriteLine(watch.ElapsedMilliseconds);

            System.Environment.Exit(0);
        }
    }
}
