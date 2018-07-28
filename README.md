# WaniKani kanji list generator

This python script splits a given kanji list to WaniKani levels. The script works the following way:
1. Create an `api_key` file with your v1 api key in it. Make sure to have only one line in the file.
2. Run the script as `python main.sh L`, where `L` is one of the followings: `n5`, `n4`, `n3`, `n2`, `n1`, `genki`, `tobira-pre`.

## More development in the near future
- It will somehow interact based on your level, eg. gives back only the unlearnt part.
- Comparison between not only WaniKani and everything else, but between each other (eg. Genki vs. Tobira)
- More lists, like Jōyō, Frequency, Minna no Nihongo, etc.
- Uploading generated lists to the github folder, as it does not contain any personal data

## Source of kanji lists:
- [JLPT lists](http://tangorin.com/common_kanji)
- [Genki list](http://genki.japantimes.co.jp/self/genki-kanji-list-linked-to-wwkanji)
- [Tobira prerequisite list](http://tobiraweb.9640.jp/contents/%E6%BC%A2%E5%AD%97%E3%83%BB%E8%AA%9E%E5%BD%99%E6%95%99%E6%9D%90/%E6%BC%A2%E5%AD%97%E3%83%AA%E3%82%B9%E3%83%88/)
- [Tobira list](http://tobiraweb.9640.jp/contents/%E6%BC%A2%E5%AD%97%E3%83%BB%E8%AA%9E%E5%BD%99%E6%95%99%E6%9D%90/%E6%BC%A2%E5%AD%97%E7%B7%B4%E7%BF%92%E3%82%B7%E3%83%BC%E3%83%88/)
