.PHONY: all clean subdirs website website-clean man html

all: generated-sources/crm.8.aio.adoc

generated-sources:
	mkdir -p $@

generated-sources/Makefile: crm.8.adoc generated-sources
	adocxt gen-makefile < $< > $@

subdirs: generated-sources/Makefile
	$(MAKE) -C generated-sources all

generated-sources/crm.8.adoc: crm.8.adoc subdirs
	adocxt gen-include < $< > $@

generated-sources/crm.8.aio.adoc: generated-sources/crm.8.adoc generated-sources/profiles.adoc
	adocaio $< > $@

generated-sources/profiles.adoc: profiles.adoc generated-sources
	cp $< $@

generated-sources/crm.8.html: generated-sources/crm.8.aio.adoc
	asciidoc --unsafe --backend=xhtml11 $<
	mv generated-sources/crm.8.aio.html generated-sources/crm.8.html

website: generated-sources/crm.8.adoc
	$(MAKE) -C website-v1 all

website-clean:
	$(MAKE) -C website-v1 clean

man: crmsh_crm_report.8 generated_sources/crm.8

generated_sources/crm.8: generated-sources/crm.8.aio.adoc
	a2x -f manpage $<

crmsh_crm_report.8: crmsh_crm_report.8.adoc
	a2x -f manpage $<

html: generated-sources/crm.8.html crmsh_crm_report.8.html

crmsh_crm_report.8.html: crmsh_crm_report.8.adoc
	asciidoc --unsafe --backend=xhtml11 $<

clean:	website-clean
	$(RM) -r generated-sources crmsh_crm_report.8 crmsh_crm_report.8.html
