# tezos_repl
a repl for michelson, tezos smart contract language

This is just a simple repl in python to interact with a michelson stack machine.  This will allow experimentation, and as it matures you should be able to define multiple contracts and have them interact.

Works for python3.

### TODO:

    - Add specialized Tezos Data Types
    - Fix (Add, Sub, Mul) types
    - Annotations
    - Macros
    - Domain Specific Types
    - Operations on contracts
    - Operations on mutez
    - Operations on timestamps
    - Cryptographic primitives
    - Compare Syntactic Sugar
    - Assertion Macros
    - Improve Parser for indentation
    - Improve Data Type Model

I'm adding some stuff for debugging.  Calling `%PRINT%;` will print the stack in your contract to stdout.  It parses like regular logic.

Example Command:
    python main.py --file add_to_store.tz --parameter "Nat(3)" --storage "Nat(10)"
