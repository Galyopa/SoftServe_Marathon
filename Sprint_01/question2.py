"""John wants to filter all the verses in a specific chapter in the Bible by the verse id. The Bible has 66 books, each book has a lot of chapters, and each chapter has a lot of verses.

The pattern of the id is bbcccvvv, where:

bb is the Book ID. (01 < bb <= 66);
ccc is the Chapter ID. (001 <= ccc);
vvv is the Verse ID. (001 <= vvv).
John wants to find verses that belong to the Book and Chapter, given by their IDs.

Example:
If John's scriptures are ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"], then
filterBible(scripture, "01", "001") => ["01001001","01001002"]

[input] array.string scripture

An array of the scriptures' ids, sorted by ASC.

[input] string book

Book id (2 letters)

[input] string chapter

Chapter id (3 letters)

[output] array.string

A filtered array with verses from the given chapter in the given book of the Bible."""

filterBible = lambda s, b, c: [i for i in s if i[:5] == b + c]

# def filterBible(scripture, book, chapter):
#     l = []
#     for s in scripture:
#         if s[:5] == book + chapter:
#             l.append(s)
#     return l


scripture = ["01001001",
             "01001002",
             "01002001",
             "01002002",
             "01002003",
             "02001001",
             "02001002",
             "02001003",
             "66022021"]
book = "01"
chapter = "001"
print(filterBible(scripture,
                  book,
                  chapter))

scripture = ["01001001",
             "01001002",
             "01002001",
             "01002002",
             "01002003",
             "02001001",
             "02001002",
             "02001003",
             "66022021"]
book = "01"
chapter = "002"
print(filterBible(scripture,
                  book,
                  chapter))

scripture = ["01001001",
             "01001002",
             "01002001",
             "01002002",
             "01002003",
             "02001001",
             "02001002",
             "02001003",
             "66022021"]
book = "02"
chapter = "001"

print(filterBible(scripture,
                  book,
                  chapter))
