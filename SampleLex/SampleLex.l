/* Lex program to count number of words */
%{
    #include<stdio.h>
    #include<string.h>
    int i = 0;
%}

/* Rules Section*/
%%
([a-zA-Z0-9])*    {i++;} /* Rule for counting number of words*/

"\n" {printf("%d\n", i); i = 0;}

[^\n] ;
%%

/* C Code Section */
int yywrap(void)
{
    return 0;
}

int main()
{
    // The function that starts the analysis
    yylex();
    return 0;
}
