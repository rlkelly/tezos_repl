# tezos_repl
a repl for michelson, tezos smart contract language

This is just a simple repl in python to interact with a michelson stack machine.  This will allow experimentation, and as it matures you should be able to define multiple contracts and have them interact.  Written in python3.


### TODO:
    - Syntactic Sugar (nested pairs, destructuring, accessing)
    - (SET_CAR, SET_CDR, IF_SOME, SET_C[AD]+R, MAP_CAR, MAP_CDR, MAP_C[AD]+R)
    - Check Domain Specific Types
    - Improve Data Type Model
    - Operations on contracts
    - Improve Parser for Indentation
    - Annotations

I'm adding some stuff for debugging.  Calling `%PRINT%;` will print the stack in your contract to stdout.  It parses like regular logic.

Example Command:
    python main.py --file add_to_store.tz --parameter "Nat(3)" --storage "Nat(10)"
