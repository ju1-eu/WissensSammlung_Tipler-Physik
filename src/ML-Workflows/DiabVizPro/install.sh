#!/bin/bash

# install.sh
echo "🚀 DiabVizPro Installation startet..."

# Prüfe Python Installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 ist nicht installiert."
    echo "Bitte installieren Sie Python 3 von python.org"
    exit 1
fi

# Prüfe ob bereits in einer virtuellen Umgebung
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Virtuelle Umgebung bereits aktiv in:"
    echo "   $VIRTUAL_ENV"
    
    # Frage ob neue Installation gewünscht
    read -p "🤔 Möchten Sie trotzdem eine neue Installation durchführen? (j/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Jj]$ ]]; then
        echo "👋 Installation abgebrochen"
        exit 1
    else
        # Deaktiviere aktuelle venv
        echo "🔄 Deaktiviere aktuelle virtuelle Umgebung..."
        deactivate
    fi
fi

# Prüfe ob venv Verzeichnis existiert
if [ -d "venv" ]; then
    echo "📂 Virtuelles Umgebungsverzeichnis existiert bereits"
    read -p "🤔 Möchten Sie es löschen und neu erstellen? (j/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Jj]$ ]]; then
        echo "🗑️  Lösche alte virtuelle Umgebung..."
        rm -rf venv
    else
        echo "👋 Installation abgebrochen"
        exit 1
    fi
fi

# Erstelle virtuelle Umgebung
echo "📦 Erstelle neue virtuelle Umgebung..."
python3 -m venv venv

# Aktiviere virtuelle Umgebung
echo "🔄 Aktiviere virtuelle Umgebung..."
source venv/bin/activate

# Prüfe ob Aktivierung erfolgreich
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "❌ Aktivierung der virtuellen Umgebung fehlgeschlagen!"
    exit 1
fi

# Upgrade pip
echo "⬆️  Upgrade pip..."
pip install --upgrade pip

# Prüfe ob requirements.txt existiert
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt nicht gefunden!"
    exit 1
fi

# Installiere Abhängigkeiten
echo "📚 Installiere Abhängigkeiten..."
if ! pip install -r requirements.txt; then
    echo "❌ Installation der Abhängigkeiten fehlgeschlagen!"
    exit 1
fi

# Installiere Paket
echo "🔨 Installiere DiabVizPro..."
if ! pip install -e .; then
    echo "❌ Installation von DiabVizPro fehlgeschlagen!"
    exit 1
fi

# Erstelle Output-Verzeichnis
echo "📁 Erstelle Output-Verzeichnis..."
mkdir -p output

echo "✅ Installation erfolgreich abgeschlossen!"
echo ""
echo "Python Version: $(python --version)"
echo "Pip Version: $(pip --version)"
echo ""
echo "Installierte Pakete:"
pip list
echo ""
echo "🚀 Zum Starten:"
echo "1. source venv/bin/activate   (falls noch nicht aktiviert)"
echo "2. python -m diabvizpro"
echo ""
echo "💡 Zum Deaktivieren der virtuellen Umgebung:"
echo "   deactivate"