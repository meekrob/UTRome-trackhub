#!/usr/bin/env python3
import sys
#WBGene	name	cosmid	chr	strand	Mangone et al.	Jan et al.	# 3'UTR isoforms	UTR_start	UTR_stop	UTR_length	PAS	PAS distance from cleavage	Cluster coverage	Description

fname = "Supplemental_Table_S5.txt"

h = {}

do_this_many = 9

with open(fname) as infile:
    for i, fieldname in enumerate(infile.readline().strip().split("\t")):
        h[fieldname] = i

    print(h.keys(), file=sys.stderr)

    for line_num, line in enumerate(infile):
        fields = line.strip().split("\t")
        chrom = 'chr' + fields[h['chr']]
        UTR_start = int( fields[h['UTR_start']] )
        UTR_end = int( fields[h['UTR_stop'] ] )
        UTR_length = int( fields[h['UTR_length'] ] )
        PAS = fields[h['PAS']]
        PAS_dist = int( fields[h['PAS distance from cleavage']] )
        name = fields[h['name']]
        strand = fields[h['strand']]

        if PAS == 'n/a':
            len_PAS = 0
        else:
            len_PAS = len(PAS)

        if UTR_end < UTR_start:
            UTR_end = int( fields[h['UTR_start']] )
            UTR_start = int( fields[h['UTR_stop'] ] )
            thickStart = UTR_start + PAS_dist
            thickEnd = thickStart + len(PAS)
        else:
            thickStart = UTR_end - PAS_dist + 1
            thickEnd = thickStart + len(PAS)

        if PAS == 'n/a':
            thickStart = UTR_start
            thickEnd = UTR_end

        #specified_len = abs(UTR_end - UTR_start)
        #if specified_len != UTR_length:
        #   print(f"warning: {chrom}:{UTR_start}-{UTR_end} ({specified_len}), {name},{PAS} does not span the specified {UTR_length=}", file=sys.stderr)
        if thickEnd > UTR_end:
            print(f"warning: {thickEnd=} {chrom}, {UTR_start}, {UTR_end}, {name} out of range", file=sys.stderr)
            continue
        if thickStart < UTR_start:
            print(f"warning: {thickStart=} {chrom}, {UTR_start}, {UTR_end}, {name} out of range", file=sys.stderr)
            continue
        
        print(chrom, UTR_start, UTR_end, name, "1000", strand, thickStart, thickEnd, "0,0,0", sep="\t")

        """
        if do_this_many:
            do_this_many -= 1
        else:
            break
        """
        
    
