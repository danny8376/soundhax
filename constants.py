"""Python constants."""

STAGE2_SIZE = 0x300
OTHERAPP_CODE_VA = 0x00101000

"""
code_image_size

The size of the loaded image containing .text+.rodata+.data.
"""

"""
fake_free_chunk

2nd dword needs to be big enough, and it is.
4th dword is null so it looks like the tail of the list is empty.

0x15D62F10:  0x15D62F48 ; don't care
0x15D62F14:  0x15D62F54 ; >= desired size
0x15D62F18:  0x00000000 ; prev, don't care as it will end up overwritten
0x15D62F1C:  0x00000000 ; next = NULL
"""

"""
fake_free_chunk_padding

Number of stack bytes that need to be inserted before we control pc.
"""

"""
sleep_gadget

.text:001B5A5C                 LDMFD           SP!, {R4-R6,LR}
.text:001B5A60                 B               sleep
"""

"""
gpu_flushcache_gadget

.text:002E2954                 STMFD           SP!, {R4-R6,LR}
.text:002E2958                 MOV             R4, R0 <- jump here
.text:002E295C                 LDR             R0, =dword_30CF2C
.text:002E2960                 MOV             R6, R1
.text:002E2964                 LDR             R5, [R0]
.text:002E2968                 BL              unknown_libname_289
.text:002E296C                 MOV             R3, R6
.text:002E2970                 MOV             R2, R4
.text:002E2974                 MOV             R1, R5
.text:002E2978                 LDMFD           SP!, {R4-R6,LR}
.text:002E297C                 B               sub_2E978C
"""

"""
gpu_enqueue_gadget

.text:002E96FC                 BL              gsp__GetInterruptReceiver
.text:002E9700                 ADD             R0, R0, #0x58
.text:002E9704                 ADD             R1, SP, #4
.text:002E9708                 BL              gsp__EnqueueGpuCommand
.text:002E970C                 ADD             SP, SP, #0x24
.text:002E9710                 LDMFD           SP!, {R4-R11,PC}
"""

constants_pre_21 = {
    "code_image_size": {
        "usa": 0x00272000,
        "eur": 0x00272000,
        "jpn": 0x00272000,
        },
    "fake_free_chunk": {
        "usa": 0x15D7AC80,
        "eur": 0x15D7AC80,
        "jpn": 0x15D7AC80,
        },
    "fake_free_chunk_padding": {
        "usa": 0x14,
        "eur": 0x14,
        "jpn": 0x14,
        },
    "heapctx": {
        "usa": 0x00395560,
        "eur": 0x00395580,
        "jpn": 0x00395520,
        },
    "sleep_gadget": {
        "usa": 0x002F0CD4,
        "eur": 0x002F0E44,
        "jpn": 0x002F0BAC,
        },
    "gpu_flushcache_gadget": {
        "usa": 0x002E5278,
        "eur": 0x002E53E8,
        "jpn": 0x002E5150,
        },
    "gpu_enqueue_gadget": {
        "usa": 0x002EAEFC,
        "eur": 0x002EB06C,
        "jpn": 0x002EADD4,
        },
    "memcpy_gadget": {
        "usa": 0x0022CDE0,
        "eur": 0x0022CF70,
        "jpn": 0x0022CDE0,
        },
    "pop_r0_pc": {
        "usa": 0x002E8DA4,
        "eur": 0x002E8F14,
        "jpn": 0x002E8C7C,
        },
    "pop_r1_pc": {
        "usa": 0x0022A644,
        "eur": 0x0022A7D4,
        "jpn": 0x0022A644,
        },
    "payload_stack_addr": {
        "usa": 0x15D7AD90,
        "eur": 0x15D7AD90,
        "jpn": 0x15D7AD90,
        },
    "stage2_code_va": {
        "usa": 0x002F6D00,
        "eur": 0x002F6D00,
        "jpn": 0x002F6D00,
        },
    "pop_r2_thru_r6_pc": {
        "usa": 0x00107F98,
        "eur": 0x00107F98,
        "jpn": 0x00107F98,
        },
    "payload_heap_addr": {
        "usa": 0x14200000,
        "eur": 0x14200000,
        "jpn": 0x14200000,
        }
}

constants_21_22 = {
    "code_image_size": {
        # same
        "usa": 0x00278000,
        "eur": 0x00278000,
        "jpn": 0x00278000,
        },
    "fake_free_chunk": {
        # same
        "usa": 0x15D62F10,
        "eur": 0x15D62F10,
        "jpn": 0x15D62F10,
        },
    "fake_free_chunk_padding": {
        # same
        "usa": 0xCC,
        "eur": 0xCC,
        "jpn": 0xCC,
        },
    "heapctx": {
        # same
        "usa": 0x0039B560,
        "eur": 0x0039B580,
        "jpn": 0x0039B520,
        },
    "sleep_gadget": {
        "usa": 0x001B5A5C, #same, actually (!!)
        "eur": 0x002F11B0, #changed
        "jpn": 0x002F0F18, #changed
        },
    "gpu_flushcache_gadget": {
        # changed
        "usa": 0x002E2948,
        "eur": 0x002E2AB8,
        "jpn": 0x002E2820,
        },
    "gpu_enqueue_gadget": {
        # changed
        "usa": 0x002E96EC,
        "eur": 0x002E9418,
        "jpn": 0x002E95C4,
        },
    "memcpy_gadget": {
        # same
        "usa": 0x0022DB1C,
        "eur": 0x0022DB1C,
        "jpn": 0x0022DB1C,
        },
    "pop_r0_pc": {
        # changed
        "usa": 0x002E6F70,
        "eur": 0x002E70E0,
        "jpn": 0x002E6E48,
        },
    "pop_r1_pc": {
        # same
        "usa": 0x0022B6C8,
        "eur": 0x0022B6C8,
        "jpn": 0x0022B6C8,
        },
    "payload_stack_addr": {
        # same
        "usa": 0x15D630C8,
        "eur": 0x15D630C8,
        "jpn": 0x15D630C8,
        },
    "stage2_code_va": {
        # same
        "usa": 0x002F5D00,
        "eur": 0x002F5D00,
        "jpn": 0x002F5D00,
        },
    "pop_r2_thru_r6_pc": {
        # same
        "usa": 0x0021462C,
        "eur": 0x00108910,
        "jpn": 0x0021462C,
        },
    "payload_heap_addr": {
        # same
        "usa": 0x14200000,
        "eur": 0x14200000,
        "jpn": 0x14200000,
        }
}

constants_3x_and_later = {
    "code_image_size": {
        "usa": 0x00278000,
        "eur": 0x00278000,
        "jpn": 0x00278000,
        "kor": 0x00291000,
        "chn": 0x00291000,
        "twn": 0x0028D000,
        },
    "fake_free_chunk": {
        "usa": 0x15D62F10,
        "eur": 0x15D62F10,
        "jpn": 0x15D62F10,
        "kor": 0x15D69A94,
        "chn": 0x15D69A94,
        "twn": 0x15D61E14,
        },
    "fake_free_chunk_padding": {
        "usa": 0xCC,
        "eur": 0xCC,
        "jpn": 0xCC,
        "kor": 0xA4,
        "chn": 0xA4,
        "twn": 0xA4,
        },
    "heapctx": {
        "usa": 0x0039B560,
        "eur": 0x0039B580,
        "jpn": 0x0039B520,
        "kor": 0x003B4520,
        "chn": 0x003B4520,
        "twn": 0x003B0540,
        },
    "sleep_gadget": {
        "usa": 0x001B5A5C,
        "eur": 0x002F11C0,
        "jpn": 0x002F0F28,
        "kor": 0x0022EAF8, # The gadget isn't correct K/C/T so we use 1 in the called func.
        "chn": 0x0022EB3C,
        "twn": 0x0022EB28,
        },
    "gpu_flushcache_gadget": {
        "usa": 0x002E2958,
        "eur": 0x002E2AC8,
        "jpn": 0x002E2830,
        "kor": 0x0012B730,
        "chn": 0x0012B730,
        "twn": 0x0012B760,
        },
    "gpu_enqueue_gadget": {
        "usa": 0x002E96FC,
        "eur": 0x002E9428,
        "jpn": 0x002E95D4,
        "kor": 0x00131B0C,
        "chn": 0x00131B0C,
        "twn": 0x00131B3C,
        },
    "memcpy_gadget": {
        "usa": 0x0022DB1C,
        "eur": 0x0022DB1C,
        "jpn": 0x0022DB1C,
        "kor": 0x00228910,
        "chn": 0x00228954,
        "twn": 0x00228940,
        },
    "pop_r0_pc": {
        "usa": 0x002e6f80,
        "eur": 0x002E70F0,
        "jpn": 0x002E6E58,
        "kor": 0x0012FA94,
        "chn": 0x0012FA94,
        "twn": 0x0012FAC4,
        },
    "pop_r1_pc": {
        "usa": 0x0022B6C8,
        "eur": 0x0022B6C8,
        "jpn": 0x0022B6C8,
        "kor": 0x002220E0,
        "chn": 0x00222124,
        "twn": 0x00222110,
        },
    "payload_stack_addr": {
        "usa": 0x15D630C8,
        "eur": 0x15D630C8,
        "jpn": 0x15D630C8,
        "kor": 0x15D69C38,
        "chn": 0x15D69C38,
        "twn": 0x15D61FB8,
        },
    "stage2_code_va": {
        "usa": 0x002F5D00,
        "eur": 0x002F5D00,
        "jpn": 0x002F5D00,
        "kor": 0x002F5D00,
        "chn": 0x002F5D00,
        "twn": 0x002F5D00,
        },
    "pop_r2_thru_r6_pc": {
        "usa": 0x0021462C,
        "eur": 0x00108910,
        "jpn": 0x0021462C,
        "kor": 0x00148740,
        "chn": 0x00148748,
        "twn": 0x00148778,
        },
    "payload_heap_addr": {
        "usa": 0x14200000,
        "eur": 0x14200000,
        "jpn": 0x14200000,
        "kor": 0x14200000,
        "chn": 0x14200000,
        "twn": 0x14200000,
        }
}
