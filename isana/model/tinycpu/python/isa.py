from isana.isa import ISA
from isana.isa import Context

from .memory import Mem
from .register import GPR, PC
from .datatype import Imm
from .instruction import instructions


class TinyCpuContext(Context):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pre_semantic(self):
        pass

    def post_semantic(self, ins):
        is_jump = any([
            ins.is_jump, ins.is_branch, ins.is_call, ins.is_tail, ins.is_return
        ])
        if not is_jump:
            self.PC.pc = self.PC.pc + 4


class TinyCpuISA(ISA):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


isa = TinyCpuISA(
    name="tinycpu",
    registers=(
        GPR,
        PC,
    ),
    memories=(
        Mem,
    ),
    immediates=(
        Imm,
    ),
    instructions=instructions,
    context=TinyCpuContext,
)
