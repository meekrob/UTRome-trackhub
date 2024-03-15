while read -a line
do
    Acc=${line[1]}
    Desc=${line[2]}
    fname=$(ls ${Acc}*.bw)

    minmax=$(bigWigInfo $fname | cut -f 2 -d ' ' | tail -3 | head -2 | tr '\n' ' ')
    echo "track $Acc"
    echo "type bigwig $minmax"
    echo "bigDataUrl bw/$fname"
    echo "shortLabel $Desc"
    echo "longLabel $Desc"
    echo "visibility full"
    echo
done < <(grep '^-' ../README.md)
