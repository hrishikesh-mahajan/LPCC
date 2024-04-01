# How to use Lex and YACC Tools

## Generate C Code from a Lex File

```sh
lex LexFileName.l
```

OR

```sh
flex LexFileName.l
```

## To compile `lex.yy.c` on ARM-based Mac OS

```sh
gcc lex.yy.c -ll -o LexFileName
```

> Use `-ll` to link `libf` library.

## Generate C Code from a YACC file

```sh
yacc -d YACCFileName.y
```

## To compile `lex.yy.c` and `y.tab.c` on ARM-based Mac OS

```sh
gcc lex.yy.c y.tab.c -ll -o YACCFileName
```

> Use `-ll` to link `libf` library.
