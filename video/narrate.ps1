# Narrate video\script.txt with the built-in "Microsoft David Desktop" voice.
# One WAV per slide (for timing the slides) plus the full narration.
# Relaxed delivery: slightly slower rate, short pauses after each sentence.
param([int]$Rate = -1, [int]$SentencePauseMs = 350)

Add-Type -AssemblyName System.Speech
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$out = Join-Path $here "audio"
New-Item -ItemType Directory -Force $out | Out-Null

$text = Get-Content (Join-Path $here "script.txt") -Raw -Encoding UTF8
$blocks = [regex]::Split($text, "(?m)^## ") | Where-Object { $_.Trim() -ne "" }

$durations = @()
$i = 0
foreach ($b in $blocks) {
    $i++
    $lines = $b -split "`r?`n", 2
    $body = $lines[1].Trim()
    $sentences = [regex]::Split($body, "(?<=[.?!])\s+") | Where-Object { $_.Trim() -ne "" }

    $pb = New-Object System.Speech.Synthesis.PromptBuilder
    foreach ($s in $sentences) {
        $pb.AppendText($s)
        $pb.AppendBreak([TimeSpan]::FromMilliseconds($SentencePauseMs))
    }

    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $synth.SelectVoice("Microsoft David Desktop")
    $synth.Rate = $Rate
    $wav = Join-Path $out ("slide{0:D2}.wav" -f $i)
    $synth.SetOutputToWaveFile($wav)
    $synth.Speak($pb)
    $synth.Dispose()

    $bytes = (Get-Item $wav).Length
    $reader = New-Object System.IO.BinaryReader([System.IO.File]::OpenRead($wav))
    $reader.BaseStream.Seek(28, 0) | Out-Null
    $byteRate = $reader.ReadInt32()
    $reader.Close()
    $secs = [math]::Round(($bytes - 44) / $byteRate, 2)
    $durations += $secs
    "{0:D2} {1,6:N2}s  {2}" -f $i, $secs, $lines[0].Trim()
}
"TOTAL {0:N1}s" -f ($durations | Measure-Object -Sum).Sum
