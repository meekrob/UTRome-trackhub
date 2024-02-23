default: trackhub/ce11/UTRome.bb

UTRome.bed:
	python convert_to_bed.py > $@

UTRome.sorted.bed: UTRome.bed
	bedSort $^ $@

ce11.chromsizes:
	fetchChromSizes ce11 > $@

trackhub/ce11/UTRome.bb: UTRome.sorted.bed ce11.chromsizes
	bedToBigBed $^ $@
