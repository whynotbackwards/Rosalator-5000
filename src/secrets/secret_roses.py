from src.imports import random

rose_pic_1 = ["       :                       ..,,..    ...,,..",
              "      ,%,                .. ,#########::#########:,",
              "      :#%%,           ,,:',####%%%%%%##:`::%%%%####,",
              "     ,##%%%%,      ,##%% ,##%%%:::::''%' `::::%%####,",
              "     %###%%;;,   ,###%%:,##%%:::''    '  . .`:::%%###,",
              "    :####%%;;:: ,##%:' ,#%::''   .,,,..    . .`::%%%##,",
              "    %####%;;::,##%:' ,##%''  ,%%########%     . `:::%%##,",
              "    ######:::,##%:',####:  ,##%%:''     `%%,     .`::%%##,",
              "    :#####%:'##%:',#####' ,###%' ,%%%%,%%,'%,     . ::%%###,,..",
              "     #####%:,#%:'#######  %%:'%  %'  `%% %% %%,.     '::%%#######,",
              "     `####%,#%:',####### ::' %   ' ,%%%%%%, ::%%.    . '::%%######",
              "      `###'##%: ######## ,.   %%  %%,   ':: `:%%%  :  . .:::%%###'",
              "      ,,::,###  %%%%%### ::  % %% '%%%,.::: .:%%%   #.  . ::%%%#'",
              ",,,:::%%##:;#   `%%%%%## :% ,%, %   ':%%:'  #%%%' ,.:##.  ::%#'",
              "::%%#####% %%:::  :::%%% `%%,'%%     ..,,%####' :%# `::##, ''",
              "###%%::'###%::: .   `:::, `::,,%%%######%%'',::%##' ,:::%##",
              "''''   ,####%:::. .  `::%,     '':%%::' .,::%%%#'   :::%%%##,",
              "      :#%%'##%:::.  . . \"%::,,.. ..,,,,::%%%###'  ,:%%%%####'",
              "     ,###%%'###%:::: . . `::::::::::%%%#####'   ,::%####:'",
              "     %###%%;'###%::::.   .`::%%%%%%%#####:'  ,,::%%##:'",
              "     ####%;:;'####%:::::.   `:%######::'  ,,:::%%###",
              "     %####;:;'######%%::::.           ,::::%%%####'",
              "     `####%;:'`#########%%:::....,,:::%%%#######'",
              "        ;#####;;'..;;:::#########::%%#########:\"'",
              "                      ```~~~~########'''~~~",
              "                         ````~~~~~~~'''"]

rose_pic_2 = ["                            __",
              "                     ___  _// \\",
              "                   _/   \\/__|_ \\",
              "                  /  __//_/==\\_| ___",
              "                / | / /|// == \\ \\   /",
              "                |  | |\\|| //_\\ | |_/",
              "                 \\  \\ \\\\ / \\_/| || \\",
              "                  \\___/\\\\| _  ///___\\",
              "                    \\__|\\_\\=//_// _\\_|",
              "                       \\___\\_____/",
              "                      !! \\____/",
              "                     !!",
              "                      !!",
              "           ___      -(!!      __ ___ _",
              "          |\\|  \\       !!_.-~~ /|\\-  \\~-._",
              "          | -\\| |      !!/   /  | |\\- | |\\ \\",
              "           \\__-\\|______ !!  |    \\___\\|  \\_\\|",
              "     _____ _.-~/|\\     \\\\!!  \\  |  /       ~-.",
              "   /     /|  / /|  \\    \\!!    \\ /          |\\~-",
              " /  ---/| | |   |\\  |     !!                 \\__|",
              "| ---/| | |  \\ /|  /    -(!!",
              "| -/| |  /     \\|/        !!",
              "|/____ /                  !!)-",
              "                          !!"]

rose_pic_3 = ["                              ,....",
              "                           ,,''    ""-.",
              "                      .--,,'           "",",
              "                    ,.  ,'     .-, ...    `",
              "                   ,'  ,'   .-\"   P  ``.  : .,.",
              "               ,'\".'   :   ,   ,--;-,   `.,\"   `.",
              "              ,'  :    :  '    :  :  `    '-,   `.",
              "              ,  ,     :  :    :  t. ',   :  `   `",
              "             ,'  :     `. :    :   `\"'`.  :  :   :",
              "             :   :       :`.   `.     ,'  :  :    :",
              "             `.  `       : `.   `-,...( .,'  ,   ,'",
              "              :   :      :   `.      ' \"    ,'   :",
              "              `. ,\",     `.    \"----'      ,'    ,",
              "               `\", `,.    `,             .'      :",
              "                 :   `,     \"-,.,.    ,,'       ,",
              "                 `     `,.      :'---\"'       ,'",
              "                  t      `-....-td           ,'",
              "                   \"-.            \"-,,....,-\"",
              "       ,,-,.  ..      `..            :   ,.''\"----\"\",...",
              "   ,'\"\"'    \"\" `-. .    `T-..    ..-`).,,'             `.",
              " ,\"'             `\" t    ,( `\"\"\"\"   ,' '    '    ,      `\"`",
              " : --. ,   `         `.  ::       ,.       :     : ,''   .'",
              " (   `\"),  `.   -.    `. `,      .'   ,    ,   ,'`\"\"-    :",
              " : ,...t,`,.'    `     `,:`,.   '    ,'   ,\",--t       ,'",
              "  `         `.   `.  ,  `\", '   :,   :  ,.''    \"--   ,'",
              "  `,          :  ,'  `, `,` t   ::   : ,.:           .'",
              "   `  -,..---\"`'\"''.  : ,'`,`.  ::   ,\"'`\"-,...    ,,'",
              "    `,              :`'\"'  `,t  :`.,\",         '  ,'",
              "      t          ,.-`---,.. : t )' '-`-.....    -''",
              "       `. ,\"\"\"\"\"\"'      : ``.  `,\",           .'",
              "        `\"`-.          '    `,   :`,..,.,'\"\"\"\"",
              "            `-,...-,.,'       \", `,   '",
              "                                \", `,.",
              "                                 :   `,.. ,.",
              "                                  \"\"\"-t.``'`-..    ,...,",
              "                                       ``-..  `\"\"\"\"'  ,",
              "                                           `\"\"---....'"]

rose_pic_4 = ["                    \"M,        .mM\"",
              "                     IMIm    ,mIM\"",
              "                     ,MI:\"IM,mIMm",
              "          \"IMmm,    ,IM::::IM::IM,          ,m\"",
              "             \"IMMIMMIMm::IM:::::IM\"\"==mm ,mIM\"",
              "    __      ,mIM::::::MIM:::::::IM::::mIMIM\"",
              " ,mMIMIMIIMIMM::::::::mM::::::::IMIMIMIMMM\"",
              "IMM:::::::::IMM::::::M::::::::IIM:::::::MM,",
              " \"IMM::::::::::MM:::M:::::::IM:::::::::::IM,",
              "    \"IMm::::::::IMMM:::::::IM:::::::::::::IM,",
              "      \"Mm:::::::::IM::::::MM::::::::::::::::IM,",
              "       IM:::::::::IM::::::MM::::::::::::::::::IM,",
              "        MM::::::::IM:::::::IM::::::::::::::::::IM",
              "        \"IM::::::::IM:::::::IM:::::::::::::::::IM;.",
              "         \"IM::::::::MM::::::::IM::::::::::mmmIMMMMMMMm,.",
              "           IM::::::::IM:::::::IM::::mIMIMM\"\"\"\". .. \"IMMMM",
              "           \"IM::::::::IM::::::mIMIMM\"\". . . . . .,mM\"   \"M",
              "            IMm:::::::IM::::IIMM\" . . . . . ..,mMM\"",
              "            \"IMMIMIMMIMM::IMM\" . . . ._.,mMMMMM\"",
              "             ,IM\". . .\"IMIM\". . . .,mMMMMMMMM\"",
              "           ,IM . . . .,IMM\". . . ,mMMMMMMMMM\"",
              "          IM. . . .,mIIMM,. . ..mMMMMMMMMMM\"",
              "         ,M\"..,mIMMIMMIMMIMmmmMMMMMMMMMMMM\"",
              "         IM.,IMI\"\"\"        \"\"IIMMMMMMMMMMM",
              "        ;IMIM\"                  \"\"IMMMMMMM",
              "        \"\"                         \"IMMMMM",
              "                                     \"IMMM",
              "                                      \"IMM,",
              "                                       \"IMM",
              "                                        \"MM,",
              "                                         IMM,              ______   __",
              "                        ______           \"IMM__        .mIMMIMMIMMIMMIMM,",
              "                   .,mIMMIMMIMM, ,mIMM,   IMM\"\"\"     ,mIM\". . . . \"IM,..M,",
              "                 ,IMMM' . . . \"IMM.\\ \"M,  IMM      ,IM\". . . .  / :;IM \\ M,",
              "               .mIM' . . .  / .:\"IM.\\ MM  \"MM,    ,M\". . .  / .;mIMIMIM,\\ M",
              "              ,IM'. . .  / . .:;,IMIMIMMM  IMM   ,M\". .  / .:mIM\"'   \"IM,:M",
              "             ,IM'. . . / . .:;,mIM\"  `\"IMM IMM   IM. .  / .mM\"         \"IMI",
              "            ,IM . .  / . .:;,mIM\"      \"IMMMMM   MM,.  / ,mM            \"M'",
              "            IM'. .  / . .;,mIM\"          \"IIMMM ,IMIM,.,IM\"",
              "            IM . . / . .,mIM\"              IMMMMMMM' \"\"\"",
              "            `IM,.  / ;,mIM\"                 IIMMM",
              "             \"IMI, /,mIM\"                 __IMMM",
              "               \"IMMMM\"                   \"\"\"IMM",
              "                 \"\"                         IMM",
              "                                            IMM__",
              "                                            IMM\"\"\"",
              "                                            IMM",
              "                                            IMM",
              "                                          __IMM",
              "                                         \"\"\"IMM",
              "                                            IMM",
              "                                            IMM",
              "                                            IMM__",
              "                                            IMM\"\"\"",
              "                                            IMM",
              "                                            IMM"]

rose_pic_5 = ["             __",
              "        _   /  |",
              "       | \\  \\/_/",
              "       \\_\\| / __",
              "          \\/_/__\\           .--='/~\\",
              "   ____,__/__,_____,______)/   /{~}}}",
              "   -,-----,--\\--,-----,---,\'-' {{~}}",
              "           __/\\_            '--=.\\}/",
              "          /_/ |\\\\",
              "               \\/"]

rose_pic_6 = ["    _,--._.-,",
              "   /\\_r-,\\_ )",
              ".-.) _;='_/ (.;",
              " \\ \\'     \\/S )",
              "  L.'-. _.'|-'",
              " <_`-'\\'_.'/",
              "   `'-._( \\",
              "    ___   \\\\,      ___",
              "    \\ .'-. \\\\   .-'_. /",
              "     '._' '.\\\\/.-'_.'",
              "        '--``\\('--'",
              "              \\\\",
              "              `\\\\,",
              "                \\|"]

rose_pic_7 = ["                                        H   H",
              "                          H           H   H   H           H",
              "                        H   H       H   H   H   H       H   H",
              "                          H   H       H   H   H       H   H",
              "                H       H   H       H   H   H   H       H   H       H",
              "              H   H       H   H       H   H   H       H   H       H   H",
              "                H   H   H   H   H       H   H       H   H   H   H   H",
              "              H   H       H   H   H       H       H   H   H       H   H",
              "                H   H       H   H   H           H   H   H   H   H   H",
              "              H   H   H       H   H   H       H   H   H   H       H   H",
              "@               H   H   H       H   H   H   H   H   H   H       H   H",
              " @ @          H   H   H   H       H   H   H   H   H   H       H   H   H",
              "    @ @         H   H   H   H   H   H   H   H   H   H   H       H   H",
              "     @ @ @        H   H   H       H   H   H   H   H   H       H   H   H",
              "        @ @     H   H   H   H       H   H   H   H   H       H   H   H",
              "         @ @ @    H   H   H           H   H   H   H       H   H   H    @ @",
              "          @ @   H   H   H   H   @   H   H   H           H   H   H   @ @ @ @ @",
              "         @ @      H   H   H    @ @    H   H           H   H   H    @ @ @   @ @",
              "        @ @ @   H   H   H   H   @ @     H       H   H   H   H     @ @ @",
              "         @ @  H   H   H   H      @ @          H   H   H   H   H    @ @ @",
              "          @     H   H   H   H   @ @ @   H   H   H   H   H   H     @ @ @",
              "              H   H   H   H      @ @      H   H   H   H   H   H    @ @",
              "                H   H   H   H     @ @       H   H   H   H   H     @ @ @",
              "     @ @ @        H   H   H   H    @ @    H   H   H   H   H   H    @ @",
              "  @ @ @ @ @ @       H   H   H     @ @ @     H   H   H   H   H     @ @ @",
              " @ @     @ @ @        H   H   H    @ @ @      H   H   H   H      @ @ @",
              "  @       @ @ @ @   H   H   H   H   @ @ @   H   H   H   H   H   @ @ @",
              "             @ @ @    H   H   H    @ @ @ @    H   H   H   H    @ @ @ @",
              "              @ @ @     H   H   H   @ @ @   H   H   H   H     @ @ @",
              "                 @ @ @    H   H    @ @ @ @    H   H   H      @ @",
              "                    @ @     H   H   @ @ @ @     H   H       @ @ @",
              "                     @ @ @    H    @ @ @ @ @  H          @ @ @",
              "                      @ @ @       @ @ @ @ @ @   @ @ @ @ @ @ @",
              "                       @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @",
              "                          @ @ @ @ @ @ @ @ @ @ @ @ @ @ @",
              "                             @ @ @ @ @ @ @ @ @ @",
              "                                  @ @ @ @ @ @",
              "                                   @ @ @ @ @",
              "                                      @ @ @",
              "             @ @ @                   @ @ @",
              "              @ @ @ @ @ @             @ @ @",
              "               @ @ @ @ @ @ @         @ @ @",
              "                @ @ @ @ @ @ @       @ @ @",
              "                 @ @ @ @ @ @ @     @ @ @   @ @ @ @ @",
              "                    @ @ @ @ @   @ @ @ @ @ @ @ @ @ @ @ @ @",
              "                         @ @   @ @ @     @ @ @ @ @ @ @ @ @",
              "                            @ @ @ @       @ @ @ @ @ @ @ @ @",
              "                         @ @ @ @             @ @ @ @ @",
              "                      @ @ @ @",
              "                   @ @ @ @"]

rose_pic_8 = ["    {\\o/}_______________________________________________________{\\o/}",
              "     )|(                                                         )|(",
              "     ~|~                                        __               ~|~",
              "      |                                     ,,-~  ~-.             |",
              "      |                                    // . -..  ~.           |",
              "      |           ____     .        \\     // '  _     }           |",
              "      |          {    }__  :.      __\\   //,'.,._ _ ,'            |",
              "      |        _/ ____ \\ \\ `::       \\\\~-:-: : : : :\\             |",
              "      |       // { __ \\ }.} :::      { @|,;: : : : : >-           |",
              "      |      /{,/ /_ \\ \\ \\ }::::     `Y'/=|_\\: : : :/             |",
              "      |     {  / // \\_\\ }//.:::'       /  |  \\-===-~              |",
              "      |     ( {_/{(@)} }.) }:<____A___/_A_|___\\,_______A_______A__|",
              "      |      \\ \\\\ \\\\/ / / };::-------v------V------v-------V------|",
              "      |       \\/\\\\_\\_/\\/_/ }`:`                                   |",
              "      |       {  { ~  } \\ /,::'                                   |",
              "      |        \\_ \\__/  /~,::'                                    |",
              "      |          {____}~ ,::'                                     |",
              "      |                  ~                                        |",
              "    {\\o/}_________________________________________________________0",
              "     )|(                                                         /V\\",
              "     ~\"~                                                          H",
              "                                                                  ^"]

rose_pic_9 = ["                         .,,.",
              "                  .,v%;mmmmmmmm;%%vv,.",
              "               ,vvv%;mmmvv;vvvmmm;%vvvv,    .,,.",
              "        ,, ,vvvnnv%;mmmvv;%%;vvmmm;%vvvv%;mmmmmmm,",
              "      ,mmmmmm;%%vv%;mmmvv;%%;vvmmm;%v%;mmmmmmmmmmm",
              "      mmmmmmmmmmm;%%;mmmvv%;vvmmm;%mmmmmmmmmmmmmm'",
              "      `mmmmmmmmmmmmmm%;mmv;vmmm;mmmmmmm;%vvvvvv'",
              "          `%%%%%;mmmmmmmm;v%v;mmmmmm;%vvvnnvv'",
              "           vvvvvv%%%%;mmmm%;mmmmmm;%vvvnnnnvv",
              "           `vvnnnnvvv%%%;m;mmmmm;%vvnnmmnnvv'",
              "            vvnmmnnnnvvv%%mmmm;%vvnnmmmnnnvv",
              "            `vvnmmmnnvvv%mmm;%vvnnmmmmnnnvv'",
              "             `vvnmmmmvv%mmm;%vvnnmmmmnnnvv'",
              "              `vvnmmmvv%mm;%vvvnnmmmnnvvv'",
              "                `vvnmmvv%m;%vvvvnmnvvvv'",
              "                 .;;vvvvvm;%vvvvvvvv'",
              "              .;;;;;;;;;;;;;;;;;;;;,",
              "             ;;;;;;';;;;;;;;;;;'`;;;;;,",
              "            .;;;'    `;;;;;;;;'   `;;;;;.",
              "           .;;'        `;;;;;'      `;;;;",
              "           ;'           :`;;'         ;;'",
              "           ;            : ;'    ,    ,'             .",
              "            `           :'.:   .;;,.        .,;;;;;;'",
              "                        ::::   ;;,;;;,     ;;;,;;;;'",
              "                        ;;;;   `;;;,;;    .,';;;;'",
              "                        ;;;;      `';; ,;;'",
              "                      ,;;;;;         .;',.",
              "                        `;;;;       .;'  ';,.",
              "                         `;;;.     .;'   ,;;,;;,.",
              "                          ;;;;    .;'    `;;;;,;;;",
              "                          ;;;;   .;'       `;;,;;'",
              "                          `;;;,;;'           `;'",
              "                           ;;;;",
              "                           ;;;;.",
              "                           `;;;;;,.",
              "                            ;;;;'",
              "                            ;;;;",
              "                            ;;;;"]

rose_pic_10 = ["                                    d\"\"\"b",
               "                                    $,,,$",
               "                                  cF\"```\"?c",
               "                                 dF       3b",
               "                                 `$.     .$'",
               "                                  `CbecedC",
               "                                  <$,   ,$>",
               "                              ,u==$F\"\"$\"\"?$==u,",
               "                           .dF\" c%\"   $   \"%c \"?b.",
               "                          c\"   J\"     $     \"o   \"c",
               "                        ,u$c,. $      $      $ .,c$u.",
               "                     ,zF\"'  `\"\"\"\"===========\"\"\"\"'  `\"?c.",
               "                  .zP\"                                 \"?o.",
               "                ,d\"                                      `\"b.",
               "              ,d\"          .,.  ,.    .                    `\"c.",
               "            .d\"       ,d$$$$$$$$$$?? ?$$$P.c$$%              `?c",
               "           d\"        ?$$$$$$ cceced$F ?$$.$$$\"<$\"              ?b",
               "         .d'          `,,c,,.\"$$$\"<PP, 3F<$$$,P`c .             `b.",
               "        ,P         .,d$$P?$$$ $$$ $F $ $$.$PF\".F',$$e.            ?,",
               "       .F         $$$$P??$cPF $$$c`$d$,???cF'cd??$$$$$.            ?,",
               "       J'         \"$$$$$hhc\"   ?$$$c `\"???% `??\"?ec,`\"              ?.",
               "      ,F              \"\"??$$b,?ccecF?c\"\"?$$c,\"\" ,bce$$$r            `b",
               "      d'                   \"?$bF\"\"\"\"?=$`$c\"$$FJ$???$$$$$ c,          $",
               "      $                ,=cec . ``\"\"\"?bc ?$$ec,. =??bcece$$$          $",
               "      $               `\"' \"  `?$$$$$$c$$ .,,,cc,`?$ec$?$$$F          $",
               "      $                      ?$c,`\"\"\"\"\"\" `?$$$$$$bc,?$$$$\"           $",
               "      $                       3$$$P\" `\"$>  `\"\"\"\"??$$$$$$$            $",
               "      $                      d\"       ,$'         `\"$$$$F            $",
               "      $                    d\"         '                \"             $",
               "      $                   z\"                                         $",
               "      $                  LP                                          $",
               "      $                  b                                           $",
               "      $                  4z         .,--==<eccr,,_                   $",
               "      $                   \"b.    ,-\"\"\"Lc.  \"?$$c$b\"4,.               $",
               "      $                     \"b. /    $r J?c. `\"\"?$$b?c\\              $",
               "      $                       ?$    d$ $$,?$P.     `\"\"?$,            $",
               "      $                        ?.   3F,l?$,\"$%.         \"            $",
               "      $                         ?   `L`b:$?,\"C4                      $",
               "      $                          3   ?.?<$J$,?$b                     $",
               "      $                           ?   ?.?F$$$ $F                     $",
               "      $                            ?.  \"=c\"?$$$$                     $",
               "      $                            `d.    \"-._\")                     $",
               "      $                             ?$        `'                     $",
               "      $                              >$                              $",
               "      $                              $3,                             $",
               "      $                              $;$                             $",
               "      $                              $$$                             $",
               "      $                              $$$                             $",
               "     ,F                              $$$                             $",
               "     d'                             ;C?F                             $",
               "    .P                              `f$                              $",
               "    d'                               ?;                              ?,",
               "   ,F                                 \"            .,,.              <b",
               "  ,F                                     .,,,. ,c$$$$$$$ec.    ,.     ?,",
               " ,F     ,ce$$$$$ec.          c.         \"\"??$$$P???$$$$$$P\",c$$$$F     ?,",
               "d\"        \"\"?$$$$$$$=--,zee  `$$$bececcc,,.  `?b`$b,  ,,cd$$$$$$$P      \"b",
               " \"\"?c,_       \"?$$$$$$$PF\"\"    \"?$$$$$$$??$$b.  \" `\"???ec,\"????\"\"     _,cF'",
               "     `\"\"??bc,_                             `\"\"           _,,,,,ccddPP\"'",
               "            `\"\"???bbcc,,..__                 ___,,ccddFFFF\"\"\"",
               "                     ``\"\"\"\"\"?????????????????\"\"\"'`"]

secret_roses = [rose_pic_1, rose_pic_2, rose_pic_3, rose_pic_4, rose_pic_5, rose_pic_6, rose_pic_7, rose_pic_8,
                rose_pic_9, rose_pic_10]


def rose_randomizer(prev_i):
    """Prints a random rose without printing any one rose twice in a row."""
    i = prev_i
    while i == prev_i:
        i = random.choice(range(len(secret_roses)))
    secret = secret_roses[i]

    return secret, i
