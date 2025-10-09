# AlexonePersonalBotV1

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Private-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](README.md)

> **⚠️ Disclaimer**: Questo è un selfbot per uso personale. L'utilizzo di selfbot potrebbe violare i Termini di Servizio di Discord. Utilizzalo a tuo rischio e pericolo.

## 📋 Indice

- [Descrizione](#descrizione)
- [Prerequisiti](#prerequisiti)
- [Installazione](#installazione)
- [Configurazione](#configurazione)
- [Utilizzo](#utilizzo)
- [Comandi Disponibili](#comandi-disponibili)
- [Risoluzione Problemi](#risoluzione-problemi)
- [Supporto](#supporto)

## 📖 Descrizione

AlexonePersonalBotV1 è un selfbot Discord personalizzato che offre una varietà di funzionalità per migliorare la tua esperienza su Discord. Il bot include comandi personalizzati, funzionalità automatizzate e molto altro.

## 🔧 Prerequisiti

Prima di iniziare, assicurati di avere:

- **Python 3.8+** installato sul tuo sistema
- **Token Discord personale** (User Token)
- **API Keys** necessarie (specificate nel file di configurazione)
- Connessione internet stabile

## 🚀 Installazione

### Passo 1: Clona o scarica il progetto
```bash
git clone [repository-url]
cd AlexonePersonalBotV1
```

### Passo 2: Installa le dipendenze
```bash
pip install -r requirements.txt
```

### Passo 3: Configura il bot
1. Apri il file `CONFIG.txt`
2. Inserisci tutte le informazioni richieste seguendo i commenti nel file
3. Salva le modifiche

## ⚙️ Configurazione

Il file `CONFIG.txt` contiene tutte le impostazioni necessarie:

```txt
// Your personal token if you don't know how to do it, ask me in dm.
TOKEN=

[MAINTENANCE] // Our SelfBot has OpenAI integrated for autoreply, pls put yours here. ( example. sk-xxxxxxxxxxxxxxxxxxxx )
[MAINTENANCE] // OPENAI_API_KEY=

// Your Personal Paypal Email or a link ( Recommended Email to bypass antilink bots ).
PAYPAL_EMAIL=

# Altre configurazioni...
```

> **🔒 Sicurezza**: Non condividere mai il tuo token Discord o le API keys con nessuno!

## 🎮 Utilizzo

### Avvio del Bot

Esegui uno dei seguenti comandi nel terminale:

```bash
# Windows
py main.py

# Linux/Mac
python3 main.py
```

### Primo Avvio

1. Avvia il bot seguendo le istruzioni sopra
2. Controlla il terminale per eventuali errori
3. Una volta avviato, digita `.help` in Discord per vedere tutti i comandi disponibili

## 📝 Comandi Disponibili

| Comando | Descrizione |
|---------|-------------|
| `.help` | Mostra tutti i comandi disponibili |
| `.afk` | Mette il proprio stato in afk |
| `.info` | Informazioni sul bot |

> Per la lista completa dei comandi, utilizza `.help` dopo aver avviato il bot.

## 🔧 Risoluzione Problemi

### Problemi Comuni

**❌ Errore: ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**❌ Errore: Token non valido**
- Verifica che il token nel `CONFIG.txt` sia corretto
- Assicurati di non aver incluso spazi extra

**❌ Il bot non risponde**
- Controlla la connessione internet
- Verifica che il token sia ancora valido
- Riavvia il bot

### Log degli Errori

Il terminale mostrerà tutti gli errori e i problemi. Se incontri errori persistenti:

1. Copia il messaggio di errore completo
2. Controlla la sezione [Supporto](#supporto)
3. Contatta lo sviluppatore se necessario

## 📞 Supporto

Se hai problemi o domande:

- **Sviluppatore**: @alex1dev
- **Discord DM**: `alex1dev`
- **Problemi di licenza**: Contatta via DM

> **📧 Prima di contattare**: Assicurati di aver seguito tutti i passaggi di installazione e configurazione.

## 📄 Licenza

Questo software è distribuito sotto licenza privata. L'utilizzo è limitato agli acquirenti autorizzati.

---

**Grazie per l'acquisto!** 🎉

*Realizzato con ❤️ da @alex1dev*
