# ripsubs

Because I'm so so lazy, I thought it'd be really nice to be able to just slice all of the embedded
subtitles out of an MP4 and boom, you have a full transcript.

It's not really that useful right now but it tapes together a few commands and a quick script to
sanitize the SRT to be just plaintext.

## Example

```bash
ripsubs.sh subtitle-movie-name.mp4
# ignore ffmpeg output
cat subtitle-movie-name.mp4.SUBTITLES.txt
# awesome text
```

## Requirements

* ffmpeg
* unix, lol
