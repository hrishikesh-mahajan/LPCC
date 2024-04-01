%{
/* This is the first lex program */
%}

%%
[ \t\r\n\f]+ ;

I |
He |
She |
We { printf("%s - Noun\n", yytext); }


is |
am |
are |
ran |
running { printf("%s - Verb\n", yytext); }

quickly |
slowly { printf("%s - Adverb\n", yytext); }

happy |
sad { printf("%s - Adjective\n", yytext); }

[a-zA-Z]+ { printf("%s - Invalid token\n", yytext); }

. { printf("%s - Special character\n", yytext); }
%%

int yywrap(void)
{
    return 0;
}

int main ()
{
    yylex();
    yywrap();
    return 0;
}