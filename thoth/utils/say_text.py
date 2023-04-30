from gtts import gTTS
import tempfile
import subprocess

def say_text(text, lang='en'):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=text, lang=lang)
        tts.save(fp.name)

        subprocess.call(['mpg123', fp.name])

if __name__ == '__main__':
    stdout_result = "Hello, this is a test."

    say_text(stdout_result)