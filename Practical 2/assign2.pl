% ==========================================
% SIMPLE AUTO DIAGNOSTIC SYSTEM
% Save as: auto.pl
% Run command: ?- start.
% ==========================================

% --- MAIN ENTRY POINT ---
start :-
    writeln('--- CAR DIAGNOSTIC SYSTEM ---'),
    writeln('Answer with y. or n.\n'),
    diagnose.

% --- DIAGNOSIS RULES ---
diagnose :-
    ask('Does the car fail to start'),
    ask('Does the engine refuse to crank'),
    !,
    writeln('\n-> RESULT: Dead or weak battery.').

diagnose :-
    ask('Does the car fail to start'),
    ask('Do you hear a clicking sound'),
    !,
    writeln('\n-> RESULT: Faulty starter motor.').

diagnose :-
    ask('Does the engine sputter'),
    ask('Is there poor acceleration'),
    !,
    writeln('\n-> RESULT: Clogged fuel filter or fuel starvation.').

diagnose :-
    ask('Does the engine sputter'),
    !,
    writeln('\n-> RESULT: Fouled spark plugs / ignition misfire.').

diagnose :-
    writeln('\n-> RESULT: Unable to determine the issue. Consult a mechanic.').

% --- HELPER LOGIC ---
ask(Question) :-
    format('~w? (y/n): ', [Question]),
    read(Response),
    Response == y.