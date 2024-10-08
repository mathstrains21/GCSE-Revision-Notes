## Architecture of the CPU

The CPU is the brain of the computer.
It processes the data and instructions that make a computer work.

Most CPU's use the Von Neumann architecture, designed in 1945.
The CPU runs programs stored in memory.
Programs consist of instructions and data, stored in memory addresses.
Only one memory is used, to store both the data and the instructions.

### Fetch-Execute Cycle

|Step   |Actions|
|-------|-------|
|Fetch  |<ol><li>The memory address is copied from the program counter to the MAR</li> <li>The instruction in the MAR is copied to the MDR</li> <li>The program counter is incremented to point to the address of the next instruction, ready for the next cycle</li></ol>|
|Decode |<ol><li>The instruction in the MDR is decoded by the CU</li> <li>The CU can get ready for the next step by loading values into the MAR or the MDR</li></ol>|
|Execute|<ol><li>The instruction is performed</li><li>This could be loading data from or writing data to memory, doing a calculation or logic operating in the ALU, changing the address in the PC, or stopping the program</li></ol>|

### Common CPU Components

|Component                    |Function|
|-----------------------------|--------|
|Arithmetic & Logic Unit (ALU)|<ul><li>This does all the calculation and logic operations</li> <li>It can do simple addition and subtraction, do multiplication and division using repeated addition/subtraction, and can compare the size of numbers</li> <li>It can also perform logic operations like AND, OR, NOT, and can do binary shifts</li> <li>It contains the accumulator register, where the output of all the ALU's operations is sent</li></ul>|
|Control Unit (CU)            |<ul><li>This is in overall control of the CPU</li> <li>It manages the fetch-execute cycle</li> <li>It controls the flow of data inside and outside the CPU</li></ul>|
|Cache                        |<ul><li>This is very fast memory inside the CPU, which is slower than the registers, but is faster than RAM</li> <li>It stores regularly used data so that the CPU can access it quickly when it's needed</li> <li>They have low capacity and are expensive compared to RAM or Secondary Storage</li> <li>There are 3 levels of cache – L1, L2, & L3. L1 is the quickest with the smallest capacity, while L3 is the slowest with the most capacit.</li></ul>|
|Registers                    |<ul><li>Memory locations inside the CPU which cab be used to temporarily store tiny bits of data the CPU needs.</li> <li>They are extremely quick to read/write to</li> <li>The most important registers are listed below</li></ul>|

### CPU Registers

|Register                     |Content|Purpose|
|-----------------------------|-------|-------|
|Memory Address Register (MAR)|Address|This holds any memory address about to be used by the CPU, which might be data or an instruction.|
|Memory Data Register (MDR)   |Data   |This holds a data or instruction, which may have been fetched from memory or waiting to be written to memory.|
|Program Counter (PC)         |Address|This keeps track of the memory address of the instruction for each cycle.|
|Accumulator (ACC)            |Data   |This stores the result of every calculation in the ALU.|
