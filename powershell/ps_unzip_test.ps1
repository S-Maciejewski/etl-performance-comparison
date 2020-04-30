
function unzipAndFilterData {
    # Expand-Archive ./randomized_data_00.zip .
    $data = Get-Content ./test_out.csv
    Write-Output "got content"

    foreach ($line in $data){
        if($line -match '"(N|M)"*') {
            Write-Output $line
        }
    }
}

unzipAndFilterData

# Measure-Command { unzipAndFilterData }
# Measure-Command { Expand-Archive ./randomized_data_00.zip . }
