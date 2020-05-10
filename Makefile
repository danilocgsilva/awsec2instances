BIN ?= awsec2instances
PREFIX ?= /usr/local

install:
	cp $(BIN).py $(PREFIX)/bin/$(BIN)
	chmod +x $(PREFIX)/bin/$(BIN)
	mkdir $(PREFIX)/bin/$(BIN)_includes
	cp $(BIN)_includes/fn.py $(PREFIX)/bin/$(BIN)_includes/fn.py
	cp $(BIN)_includes/DataIterator.py $(PREFIX)/bin/$(BIN)_includes/DataIterator.py
	cp $(BIN)_includes/Talk.py $(PREFIX)/bin/$(BIN)_includes/Talk.py

uninstall:
	rm -rf $(PREFIX)/bin/$(BIN)
	rm -rf $(PREFIX)/bin/$(BIN)_includes
