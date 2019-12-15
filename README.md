# WaniKani kanji list generator

The `list.py` python script splits a given kanji list to WaniKani levels. The script works the following way:
1. Create an `api_key` file with your v1 api key in it. Make sure to have only one line in the file.
2. Run the script as `python list.py L`, where `L` is one of the followings: `n5`, `n4`, `n3`, `n2`, `n1`, `genki`, `tobira-pre`, `tobira` and `shiru-i` where i is a number between 1-11.
To create your own list of kanji out of text I recommend using the `text_to_kanjilist.py` script, which strips hiragana, katakana, latin alphabet, and removes repeating kanji.

## More development in the near future
- It will somehow interact based on your level, eg. gives back only the unlearnt part.
- Comparison between not only WaniKani and everything else, but between each other (eg. Genki vs. Tobira)
- More lists, like Jōyō, Frequency, Minna no Nihongo, etc.
- Uploading generated lists to the github folder, as it does not contain any personal data

## Source of kanji lists
- [JLPT lists](http://tangorin.com/common_kanji)
- [Genki list](http://genki.japantimes.co.jp/self/genki-kanji-list-linked-to-wwkanji)
- [Tobira prerequisite list](http://tobiraweb.9640.jp/contents/%E6%BC%A2%E5%AD%97%E3%83%BB%E8%AA%9E%E5%BD%99%E6%95%99%E6%9D%90/%E6%BC%A2%E5%AD%97%E3%83%AA%E3%82%B9%E3%83%88/)
- [Tobira list](http://tobiraweb.9640.jp/contents/%E6%BC%A2%E5%AD%97%E3%83%BB%E8%AA%9E%E5%BD%99%E6%95%99%E6%9D%90/%E6%BC%A2%E5%AD%97%E7%B7%B4%E7%BF%92%E3%82%B7%E3%83%BC%E3%83%88/)

# WaniKani first and second wave list

The `shortlevel.py` python script splits every WaniKani level kanji list into two: the first wave is the one you get upon unlocking the level, and the second wave is the one you get after guruing the radicals. It also creates a list of levels that are "short", thus the ones where the first wave is at least 90% of the total kanji in the level.
The script works the following way:
1. Create an `api2_key` file with your v2 api key in it. Make sure to have only one line in the file.
2. Run the script as `python list.py`, and wait. It will take a while...

Or, alternatively, you can look up the result of the script that I ran on 2018-08-19 in `shortlevels_2018_08_19.txt`. 
The new short levels are in `shortlevels_2018_12_06.txt`. Unfortunately I do not have a subscription anymore (since April 2019), so if there is any changes in that, please PR me the new output, thank you!
