
.PHONY: all clean

all: output/report.pdf

raw/raw_data.csv: src/download_raw.py
	python src/download_raw.py -o $@

output/regression.tex output/scatter.pdf: raw/raw_data.csv src/analysis.py
	python src/analysis.py -i $< -o $@

output/report.pdf: report/report.tex output/regression.tex output/scatter.pdf
	cd report/ && pdflatex report.tex && mv report.pdf ../output/report.pdf

clean:
	rm -f output/*.pdf
	rm -f output/*.tex
	rm -f raw/*.csv