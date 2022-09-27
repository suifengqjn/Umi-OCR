# tbpu : text block processing unit
# 文本块处理单元

# OCR返回的结果中，一项包含文字、包围盒、置信度的元素，称为一个“文块” - text block 。
# 文块不一定是完整的一句话或一个段落。反之，一般是零散的文字。
# 一个OCR结果常由多个文块组成。
# 文块处理器就是：将传入的多个文块进行处理，比如合并、排序、删除文块。

from utils.config import Config
from ocr.tbpu.merge_line_h import TbpuLineH
from ocr.tbpu.merge_line_h_multi import TbpuLineHMulti
from ocr.tbpu.merge_line_v_lr import TbpuLineVlr
from ocr.tbpu.merge_line_v_rl import TbpuLineVrl


Tbpus = {
    '通用': None,
    '横排-优化单行': TbpuLineH,
    '横排-合并多行': TbpuLineHMulti,
    '竖排-单行-从左到右': TbpuLineVlr,
    '竖排-单行-从右至左': TbpuLineVrl,
}

Config.set('tbpu', Tbpus)