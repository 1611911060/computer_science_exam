# Values of N
$nValues = 8,10,12,15,20,30,40,50,100

# Output file
$outputFile = "results.txt"

Remove-Item $outputFile -ErrorAction SilentlyContinue

foreach ($n in $nValues) {
    "==============================" | Out-File $outputFile -Append
    "N = $n"                         | Out-File $outputFile -Append
    "==============================" | Out-File $outputFile -Append

    minizinc `
        --solver cbc `
        --statistics `
        CP_boolean.mzn `
        -D "n=$n" |
    Out-File $outputFile -Append
}
