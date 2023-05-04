# Hack Assembly Assembler

This is a simple assembler for the Hack Assembly language, which is used to program the Hack platform as part of the Nand2Tetris course. This assembler is designed to take Hack Assembly language source code as input and produce binary machine code that can be executed on the Hack platform. In addition to the original functionality, this version also allows you to compile VM code or bytecode into Hack Assembly language source code.

## Installation

To use the assembler, you'll need to have Python 3 installed on your computer. You can download the latest version of Python from the official Python website: https://www.python.org/downloads/

Once you have Python installed, you can download the assembler source code from this repository by running:

```
git clone https://github.com/NathanSelig/HackAssembly
```

## Usage

### Assembling Hack Assembly Language Code

To assemble a Hack Assembly language source file, you can run the following command:

```
python3 Assembler.py <input_file.asm> <output_file.bin>
```

Where `<input_file.asm>` is the name of the input file containing the Hack Assembly source code, and `<output_file.bin>` is the name of the output file where the assembled binary code will be written.

For example, to assemble the `Add.asm` file and produce `Add.bin` as output, you would run:

```
python3 assembler.py Add.asm Add.bin
```

### Compiling VM Code or Bytecode to Hack Assembly Language Code

To compile VM code or bytecode to Hack Assembly language source code, you can run the following command:

```
python3 VMTranslator.py <input_file.vm> <output_file.asm>
```

Where `<input_file.vm>` is the name of the input file containing the VM code or bytecode, and `<output_file.asm>` is the name of the output file where the compiled Hack Assembly language code will be written.

For example, to compile the `SimpleAdd.vm` file and produce `SimpleAdd.asm` as output, you would run:

```
python3 VMTranslator.py SimpleAdd.vm SimpleAdd.asm
```

## Contributing

If you find any bugs or issues with the assembler, or if you would like to contribute new features or improvements, please feel free to open an issue or submit a pull request on GitHub.

## License

This assembler is licensed under the MIT license. See the `LICENSE` file for more details.

## Acknowledgements

This assembler is based on the Hack Assembly language specification and tools provided as part of the Nand2Tetris course.