%{
    #include <stdio.h>
    void yyerror(char *);
    int yylex();
%}

%token TYPE IDENTIFIER OPERATOR NUMBER SEMICOLON COMMENT

%%
start: TYPE IDENTIFIER OPERATOR NUMBER SEMICOLON COMMENT { printf("Valid Statement.\n"); }
%%

int yywrap()
{
    return 0;
}

void yyerror(char *s)
{
    printf("%s\n", s);
}

int yylex()
{
    return 0;
}

int main()
{
    printf("\nEnter C language Statement:\n");
    char yytext[1000];
    scanf("%[^\n]%*c", yytext);
    yyparse();
    yywrap();
}
