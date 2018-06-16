SELECT s1.Score as Score, (SELECT count(distinct s2.score)+1 FROM Scores s2 where s2.score >s1.score) as Rank
FROM Scores s1
ORDER BY Rank ASC