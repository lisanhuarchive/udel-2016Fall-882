all:
	python3 predict.py SanhuLi.txt SanhuLi.txt > p1.txt
	python3 predict.py charlotte/*.txt SanhuLi.txt > p2.txt
	python3 predict.py charlotte/*.txt BranchElbert.txt > p3.txt

	perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t SanhuLi.txt
	perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t SanhuLi.txt -p p1.txt
	perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t SanhuLi.txt -p p2.txt
	perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t BranchElbert.txt
	perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t BranchElbert.txt -p p3.txt
