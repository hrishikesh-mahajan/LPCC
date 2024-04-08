%{
    #include "y.tab.h"
%}

%%

"/*"([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*"*"+"/" {
    return COMMENT;
}

"//".* {
    return COMMENT;
}

[0-9]+ {
    return NUMBER;
}

int|void|double|float|char {
    return TYPE;
}

[a-zA-Z_][a-zA-Z0-9_]* {
    return IDENTIFIER;
}

"+"|"-"|"*"|"/"|"=" {
    return OPERATOR;
}

";" {
    return SEMICOLON;
}

[\n\t ]+ {
    /* Ignore whitespace, newline, tab */
}

. {
    return yytext[0];
}

%%
