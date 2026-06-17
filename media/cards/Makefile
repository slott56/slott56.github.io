PICS = $(patsubst %.puml,%.png,$(wildcard *.puml))
PLANTUML := java -jar ~/bin/plantuml-gplv2-1.2026.6.jar

all: $(PICS)

%.png: %.puml
	@echo "Convert" $< ...
	$(PLANTUML) --progress-bar --png $<

.PHONY: all
