# deep_bortox: @lucabortolussi speech imitator

Faceswap setup instructions (also for cosilt) available [here](./INSTALL.md).


## Risorse necessarie
### auditok
con auditok si spezzetta un file audio in tanti file audio (tramite un comando da prompt)
https://github.com/amsehili/auditok/blob/master/README.md

### speech recognition
con speech recognitiion dato un file audio ottieni il testo corrispondente usando vari speech recognition systems, quello offline non è molto accurato, meglio google (ci vorrebbe l'api key ma si può fare anche senza)
https://github.com/Uberi/speech_recognition/


## cosa si fa
quindi mettendo insieme i due hai per ogni parola/frase la traccia audio e viceversa, così si può trasformare un testo arbitrario in audio cercando tra le tracce che hai secondo le parole corrispondenti

Con auditok si invoca da riga di comando: auditok -i <inputFilePath> -o {N}<outputFile>

Con https://github.com/DomagojKorais/deep_bortox/blob/master/audio2text.py si invoca da riga di comando: python audio2text <directoryWithAudioFiles>
Nella cartella <directoryWithAudioFiles> ci sono uno o più file audio, viene generato un file con una riga per ciascun file audio con il nome del file ed il testo che è stato estratto dalla traccia audio usando speech recognition (google, oppure Sphinx offline)


