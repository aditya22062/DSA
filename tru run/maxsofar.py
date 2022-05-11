def solution2(words, farr, score, idx):
    if (idx == len(words)):
        return 0

    max1 = solution2(words, farr, score, idx + 1)
    max2 = 0

    isValid = True
    scoreofCW = 0
    for  ch in words[idx]:
        farr[ord(ch) - ord('a')]-=1
        if (farr[ord(ch) - ord('a')]) < 0:
            isValid = False
        scoreofCW += score[ord(ch) - ord('a')]
    if (isValid): 
        max2 = solution2(words, farr, score, idx + 1)
        max2 += scoreofCW
    
    for ch in  words[idx]:
        farr[ord(ch) - ord('a')]+=1
    return max(max1, max2)



nofWords = int(input())
words = list(input().split())

nofLetters = int(input())
letters = list(input().split())
score = list(map(int,input().split()))

if (words == None or len(words) == 0 or letters == None or len(letters) == 0 or score == None
        or len(score) == 0):
        print(0)

farr = [0]*26
for  ch in letters:
    farr[ord(ch) - ord('a')]+=1
print(solution2(words, farr, score, 0))
