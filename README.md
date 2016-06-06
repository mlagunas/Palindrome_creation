# Palindrome creation
Code developed for educational purposes during the course Basic algorithms at the university of Zaragoza. This repository has
implemented a basic palindrome creator with the dynamic programming technique. It is based on the largest palindromic subsequence problem (LPS).

## USAGE

    python palindrome.py text
    
    text is the string to transform into a palindrome
    
## RESULTS
```
Number of operations -- 1
Input string -- mannaam
Delete pos 6 -- mannam
Final result: mannam
```

```
Number of operations -- 10
Input string -- algoritmia basica
Delete pos 2 -- agoritmia basica
Delete pos 2 -- aoritmia basica
Delete pos 2 -- aritmia basica
Delete pos 2 -- aitmia basica
Delete pos 3 -- aimia basica
Delete pos 3 -- aiia basica
Delete pos 6 -- aiia asica
Delete pos 7 -- aiia aica
Change pos 8 for i -- aiia aiia
Final result: aiia aiia
```

```
Input string -- Esto es una cadena larga
Number of operations -- 17
Add a in pos 0 -- aEsto es una cadena larga
Delete pos 2 -- asto es una cadena larga
Delete pos 2 -- ato es una cadena larga
Delete pos 2 -- ao es una cadena larga
Delete pos 2 -- a es una cadena larga
Delete pos 3 -- a s una cadena larga
Delete pos 3 -- a una cadena larga
Delete pos 4 -- a na cadena larga
Delete pos 7 -- a na adena larga
Delete pos 8 -- a na aena larga
Delete pos 8 -- a na ana larga
Delete pos 9 -- a na an larga
Delete pos 10 -- a na an arga
Delete pos 10 -- a na an rga
Delete pos 10 -- a na an ga
Change pos 10 for -- a na an a
Final result: a na an a
```

```
Number of operations -- 5
Input string -- 12342331234
Delete pos 1 -- 2342331234
Delete pos 1 -- 342331234
Delete pos 2 -- 32331234
Delete pos 5 -- 3233234
Delete pos 7 -- 323323
Final result: 323323
```
