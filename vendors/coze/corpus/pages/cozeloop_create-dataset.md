> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

在评测场景中，评测集是一个精心设计的标准化测试数据集，用于系统化地评测 AI Agent 的性能。评测集通常包含输入样本和预期输出。输入样本作为评估对象的输入数据，预期输出提供了评估基准。在开始执行评测实验前，需要先准备好评测集。本文指导你在扣子罗盘中创建和管理评测集。
## 评测集介绍 {#4725a0e2}
评测集是用于评测评估对象的一组数据。它通常包含输入数据和预期的输出结果，帮助开发者验证评估对象的效果。
对于评测集中通常包含以下列：

* 输入数据（input）：这些是提供给评测对象的标准化测试样本，用于评测 AI Agent 在不同场景下的表现。
* 预期输出（reference_output）：这些是理想的结果，作为评估基准，帮助评估者或评估器对输出做出判断。
* 实际输出（actual_output）：评测对象的实际输出，通常用于线上 Trace 数据回流场景。

## 评测集限制 {#c2021a48}
设计评测集之前，你需要了解评测集文件的以下限制：

* 最多可添加 5000 条测试数据，文件大小限制为 200 MB。
* 本地上传的 CSV 文件仅支持 UTF-8 编码格式。
* 最多添加 50 个自定义列。

## 评测集设计原则 {#7f3fb208}
设计评测集的用户问题时，应注意：

* **确保核心链路通畅**：评测集需要覆盖 AI Agent 的各个功能点，尽量模拟真实的用户交互、设计典型对话，以确保 AI Agent 的表现符合产品设计和业务需求。 
* **评估范围全面**：评测集应该包含不同难度、不同领域的数据，以便全面评估模型的性能。如果包含多种任务，需要确保各个类别之间的数据量均衡，保证每种任务都有足够的样本数据。
* **覆盖极端场景和异常输入**：尝试通过评测集识别出 AI Agent 响应质量不符合预期的场景，同时也需要模拟异常输入、超限输入、违规输入的情况，判断 AI Agent 在各种场景下是否都可以按照预期执行任务。
* **确保覆盖异常案例**：对于用户反馈不合理的 AI Agent 响应案例，将其添加到测试集中，确保 AI Agent 的新版本已解决这些问题，可以按预期执行任务。

## 构建评测集 {#894f726c}
评测集构建包含创建评测集和添加测试数据两个操作。
### 步骤一：创建评测集 {#0265fa10}
参考以下步骤，创建评测集。扣子罗盘支持 **本地上传** 和 **手动导入** 两种方式来创建评测集。当前步骤介绍 **手动导入** 的方式。关于 **本地上传** 的方式，详情参见 [导入和导出评测集](/cozeloop/create-dataset#12833199)。

1. 登录 [扣子罗盘](https://loop.coze.cn)，在左侧导航栏顶部，选择你的工作空间。
2. 在左侧导航栏，选择**评测 > 评测集**，然后把鼠标移动到 **+ 新建评测集** 按钮上，在下拉菜单中单击 +**新建评测集**。
   ![Image=3786x1316](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a8bf9d9ca6184e568a5f63a20b082f6d~tplv-goo7wpa0wc-image.image)
3. 在**新建评测**集页面，参考以下信息配置评测集的数据列信息。单击 **+添加列** 可以添加自定义列。数据列信息配置完成后，单击**创建**。
   <!-- @cols-width: 100,206,630 -->
   | | | | \
   |**配置项** | |**说明** |
   |---|---|---|
   | | | | \
   |**基本信息** |**名称** |输入一个评测集名称。 |
   |^^| | | \
   | |**描述** |提供一个评测集描述。 |
   | | | | \
   |**配置列** |**选择场景一键快速配置** |你可以选择以下场景。本文仅介绍理想输出评测集的场景。 |\
   | | | |\
   | | |* **理想输出评测集**：（默认）用于评测  LLM 或 AI Agent 实际输出与预期结果的匹配程度。 |\
   | | |* **工作流评测集**：用于评测扣子工作流。详情参见 [评测扣子工作流](/cozeloop/evaluate_coze_workflow)。 |\
   | | |* **轨迹评测集**：用于评测 AI Agent 的轨迹（Trajectory）。详情参见 [通过数据回流评测行程规划 Agent 的轨迹](/cozeloop/trajectory-evaluation-tutorial)。 |
   |^^| | | \
   | |**input** |指定输入样本列配置： |\
   | | | |\
   | | |   * **名称**：输入列名称。必须以英文字母开头，支持添加字母、数字和下划线。 |\
   | | |   * **数据类型**：选择一种数据类型。通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量；同时可以提高数据的消费和存储成本。 |\
   | | |   * **查看格式**：选择一种渲染评测数据的格式，提高数据的可读性和维护性。 |\
   | | |   * **描述信息**：提供描述信息，帮助评测对象理解这个输入数据。 |
   |^^| | | \
   | |**reference_output** |指定数据集中期望输出列配置： |\
   | | | |\
   | | |   * **名称**：输入列名称。必须以英文字母开头，支持添加字母、数字和下划线。 |\
   | | |   * **数据类型**：选择一种数据类型。扣子罗盘通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量；同时可以提高数据的消费和存储成本。关于评测集数据类型的详细说明，可参考[评测集数据类型](/cozeloop/create-dataset#e9e3a87a)。 |\
   | | |   * **查看格式**：选择一种渲染评测数据的格式，提高数据的可读性和维护性。 |\
   | | |   * **描述**：提供预期输出的补充信息，可作为评估时的参考标准。 |

   系统会根据指定的数据列配置创建一个草稿版本的评测集。
   ![Image=2354x1152](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/85977391f2ac43b1b721b9cdd9fc4f07~tplv-goo7wpa0wc-image.image)

### 步骤二：添加测试数据 {#06884aed}
接下来，就可以在已创建的评测集中添加数据了。扣子罗盘支持 **本地上传**、**手动导入** 和 **智能合成** 三种方式来添加测试数据。当你需要批量上传测试数据时，选择本地上传方式。
:::tip 说明
本文档以文本数据为例。关于多模态数据，参阅 [向评测集添加多模态数据](/cozeloop/multi-modal-dataset) 。
:::

:::: tabs
@tab 手动添加
1. 在评测集详情页面，选择添加**数据 > 手动添加**来添加测试数据。
   ![Image=2900x1530](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d703ca288c304911bb450ee7a03077a9~tplv-goo7wpa0wc-image.image)
2. 在**添加数据**页面，输入第一组测试数据，然后单击 **+ 添加数据项**添加更多测试数据。最后，单击**添加**完成数据添加。
   ![Image=529x434](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/40ef987c4d0d4b3e8f675a967894843c~tplv-goo7wpa0wc-image.image)

@tab 本地上传
1. 在评测集详情页面，选择添加**数据 > 本地导入**来添加测试数据。
   ![Image=3321x1456](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5469d2898583499fba52e990606670e5~tplv-goo7wpa0wc-image.image)
2. 在 **导入本地数据** 页面，选择 **导入方式**，然后上传要导入的测试数据文件。
   你可以选择以下导入方式：
      * **数据更新与追加**：根据行 ID 和列映射更新原数据或向原数据追加新数据。
         :::notice 注意
         当你使用 **数据更新与追加** 方式导入时，导入文件必须包含 `__system_internal_id__` 列。系统将根据该列的 ID 值执行以下操作：
         
         * **更新数据**：如果文件中的 `__system_internal_id__` 与评测集中某行数据的 ID 匹配，系统将使用文件中的数据更新该行。
         * **追加数据**：如果文件中的 `__system_internal_id__` 在评测集中不存在，系统会将其作为新数据添加，并为该行自动生成一个全新的 ID。
         * **处理重复 ID**：如果导入文件中存在重复的 `__system_internal_id__`，系统将以最后一条出现的数据为准进行更新或追加。
         :::
      * **全量覆盖**：把原数据全部替换为新数据。
    上传数据前，建议你单击 **下载模版**，并使用模版中的数据格式来上传测试数据。
      ![Image=634x566](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/25366470f6e64af0bc29af579a418cf0~tplv-goo7wpa0wc-image.image)
3. 当完成数据导入后，将文件中的数据列与评测集的数据列进行映射。
   :::notice 注意
   * 如果上传的文件包含评测集中不存在的数据列，系统会自动将该列添加至评测集。
   * 由于 CSV、Excel 文件不包含数据类型信息，上传时，扣子罗盘会根据文件中每行的数据内容来校验其数据格式。如果校验不通过，该行数据将不会被上传。
      例如，CSV 文件中有一列 A，包含两行数据 `10` 和 `helloworld`。在创建评测集时，你指定了列 B 的数据类型为 **int**。当添加数据时，将 CSV 中的列 A 映射到评测集的列 B，即将 CSV 的 A 列数据导入到评测集的 B 列。在上传校验过程中，由于 B 列的数据类型为 **int**，`helloworld` 这一行数据将无法导入。
   :::
   如果导入方式为**数据更新与追加**，你需要确保：
      * 导入的数据列中包含 `__system_internal_id__` 列。
      * 列映射关系符合预期。
   ![Image=548x403](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/790f6b21fc604d95800ea5e8564d2285~tplv-goo7wpa0wc-image.image)
   如果导入方式是 **数据更新与追加**，你需要确保列映射关系符合预期。
   ![Image=610x364](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0eec8d1629cb4c1289b0d3b64ae95661~tplv-goo7wpa0wc-image.image)
4. 单击**导入**。导入完成后，扣子罗盘会弹出一个窗口，向你显示数据上传结果。
   对于上传失败的数据行，你可以根据失败原因，修改数据并重新上传。下图显示了由于数据类型不匹配导致上传失败的情况。
   ![Image=3814x1911](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f9f92fe5c4d4f11b229d3e278d8cde0~tplv-goo7wpa0wc-image.image)



@tab 智能合成
详情参阅 [智能合成评测数据](/cozeloop/dataset_ai_synthesis)。

::::

## 修改评测集 {#95901b73}
### 修改评测集基础信息 {#d2b70ab9}

* 方法一：在评测集列表页面，选中目标评测集，然后单击**修改来**修改评测集的名称和描述。
* 方法二：在评测集详情页面，单击评测集名称旁边的编辑图标修改评测集名称和描述。
   ![Image=518x104](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/763e53ff24084b1fb76739aee7e88de2~tplv-goo7wpa0wc-image.image)

### 修改数据列 {#ff8a149e}
你可以在评测集**草稿**状态下，修改评测集的列配置。
在评测集详情页面，单击**编辑列**。然后，在列配置页面，删除、增加列或修改列的数据类型。
:::notice 注意
仅当**++评测集草稿数据为0++​**时，方可修改数据类型。
:::
![Image=2382x595](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6b650aceed57496c9af012ff91160897~tplv-goo7wpa0wc-image.image)
### 修改评测集数据 {#67a9bd61}
你可以在评测集**草稿**状态下，修改评测集数据。
:::tip 说明
草稿版本的评测集数据修改不影响已提交的历史版本。如果历史版本的评测集关联了实验，也可以根据历史版本的实验回溯原版本数据。
:::

* 新增数据项：在评测集详情页面，单击**添加数据**。详细说明参考[步骤二：添加测试数据](/cozeloop/create-dataset#06884aed)。
* 修改数据项：在评测集详情页面，单击目标数据项操作列下的**编辑**，然后修改数据并保存。
   ![Image=613x151](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7570ac60c8794df083ad6ed96fb0274f~tplv-goo7wpa0wc-image.image)
* 删除数据项：
   * 单条删除：在评测集详情页面，单击目标数据项操作列下的**删除**，即可删除该条数据。
      ![Image=2368x538](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7d46319e870f415093ba80d117cffd32~tplv-goo7wpa0wc-image.image)
   * 批量删除：评测集详情页面，先单击**批量操作**，然后选择要删除的数据项，再单击**删除**即可删除所选数据项。
      ![Image=577x209](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cddee88179744e449b97d8d9c4db4a4c~tplv-goo7wpa0wc-image.image)

## 管理评测集版本 {#0a0f3e94}
评测集提供了版本管理能力，用于满足数据驱动型团队持续迭代评测数据以提高数据质量。
评测集创建后默认为草稿状态。在不同评测阶段，测试集的版本作用也不同：

* **数据完备阶段**：完成测试数据导入后，可提交首个测试版本并关联实验任务，系统将基于该版本进行全量评估。
* **评估验证阶段**：通过实验报告分析当前版本的数据表现，定位待优化数据样本。
* **优化升级阶段**：根据评估结果修正数据集后，提交升级版本并重新关联实验，开启新一轮验证循环。

这种版本机制通过"提交-评估-优化"的递进式循环，确保评测集持续满足评估迭需求。
### 新建评测集版本 {#d5d4efcf}

1. 在添加测试数据后，单击**提交新版本**。
   ![Image=2390x1072](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b377057a790a42748ffc68ee0249fd6d~tplv-goo7wpa0wc-image.image)
2. 在弹出的对话框内容，确认版本号后，再单击**提交**。

### 查看评测集历史版本 {#dd6af238}
在评测集详情页，单击**历史版本。版本记录**区域会显示全部已提交的版本，单击一个目标历史版本，就可以切换到该评测集的历史版本。
:::tip 说明
不支持修改历史版本的测试集数据。
:::
![Image=2368x1294](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a6d269f45a10426e8e2ccbc9b400b41f~tplv-goo7wpa0wc-image.image)
## 导入和导出评测集 {#12833199}
扣子罗盘支持将 Trace 数据手动沉淀到评测集。通常情况下，回流到评测集中的数据还需要经过二次处理，例如将线上真实的高质量问答对数据，沉淀为基准评测集；将评测分数低、耗时长、耗费 Token 多、应用输出不符合预期等类型的 Badcase，分类沉淀为问题数据集。
在这种场景下，你需要先把整个评测集导出到本地文件，经过二次处理后再把文件导入为评测集。
### 把本地文件导入为评测集 {#eccab037}
:::tip 说明
在上传文件时，请遵循以下限制：

* **支持格式**：.csv、.xlsx、.xls、.jsonl、.zip（.zip 文件用于多模态评测集，详情参见 [向评测集添加多模态数据](/cozeloop/multi-modal-dataset)）。
* **文件数量**：一次只能导入一个文件。
* **文件大小**：最大 500 MB。
* **数据条数**：最多 5000 条。
* **自定义列**：最多 50 个。
* **编码要求**：CSV 文件仅支持 UTF-8 编码。
:::

1. 登录 [扣子罗盘](https://loop.coze.cn)，在左侧导航栏顶部，选择你的工作空间。
2. 在左侧导航栏，选择**评测 > 评测集**，然后把鼠标移动到 **+ 新建评测集** 按钮上，在下拉菜单中单击 +**新建评测集**。
   ![Image=3340x1302](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bec4e63cba5242a098b451545bba605e~tplv-goo7wpa0wc-image.image)
3. 在 **导入本地文件** 页面的 **上传文件** 区域，单击上传区域上传或直接把文件拖拽到上传区域。为确保数据格式正确，建议你先单击 **下载模版**，并按照模版文件的格式整理数据后再上传。文件上传完成后，扣子罗盘会自动填充评测集名称、各个列名称和数据类型。
   ![Image=2424x1473](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/769d39a3f533402ab7e6d1634e115bc6~tplv-goo7wpa0wc-image.image)
4. 在 **导入本地文件** 页面的 **基本信息** 区域，输入评测集的名称和描述，并确认 **配置列** 区域的预览信息。确认无误后，单击 **创建并导入**。
   :::notice 注意
   扣子罗盘默认会把多模态和轨迹的 **数据类型** 填充为 String，因此：
   
   * 对于多模态数据，你必须手动把 **数据类型** 设置为 **多模态**。
   * 对于轨迹数据，你必须手动把 **数据类型** 设置为 **轨迹**。
   :::
   ![Image=798x726](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7435f85a5f2347858f2f09a001ddce3b~tplv-goo7wpa0wc-image.image)
5. 等待几秒钟后刷新页面。你可以看到已经被导入的数据项。
   ![Image=3330x828](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/79f19aa959e9440399d9aa1a2af2089a~tplv-goo7wpa0wc-image.image)
6. 数据内容确认无误后，单击右侧的 **提交新版本** 按钮。在弹出的窗口中，输入版本号和版本说明，然后单击 **提交**。
   ![Image=3346x1452](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e020bb2e08614578ae1e1d74449361a5~tplv-goo7wpa0wc-image.image)

### 把评测集导出为本地文件 {#e1bf6f10}

1. 登录 [扣子罗盘](https://loop.coze.cn)，在左侧导航栏顶部，选择你的工作空间。
2. 在左侧导航栏，选择**评测 > 评测集**。
3. 找到你需要导出的评测集。在 **操作** 列单击 **详情**。
4. 在评测集的详情页，单击右侧的 **...** 按钮，在下拉菜单中选择需要导入的文件格式。
   ![Image=3330x855](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/eba743f3087b44e2bc825925e803a384~tplv-goo7wpa0wc-image.image)
5. 在弹出的窗口中，选择需要导出的评测集版本，然后单击 **导出**。
   ![Image=3316x1174](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d29ca6fbe05f427988eaa4cb5f3fb513~tplv-goo7wpa0wc-image.image)
6. 文件导出完成后，在右上角的弹窗中单击 **下载文件** 把文件下载到本地。
   ![Image=3310x854](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6fa60ebdbe084b2cb2a0356ab7afbebe~tplv-goo7wpa0wc-image.image)

## 后续操作 {#a9916c40}
### 新建实验 {#607020cd}
你可以在评测数据构建完成并提交版本后，直接从评测集发起实验进行评测。
在评测集详情页，单击 **+ 新建实验**。关于实验的配置过程，参考[管理实验](/cozeloop/create-experiments)。
![Image=560x145](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/88d91aef892b44a480833ae4cf5cdee6~tplv-goo7wpa0wc-image.image)
### 关联实验 {#a206c473}
关联实验模块提供了一个聚合视图，展示与同一评测集关联的所有评测实验。你可以在此页面查看当前实验列表中各个实验在不同评估器指标下的得分。
如果需要更深入的对比分析，你可以选择多个实验并发起实验对比，以获得详细的比较结果和洞察。该方式可以帮助你更好地理解实验之间的差异和性能表现，从而支持更精准的优化和决策。详情请参考[多实验对比](/cozeloop/create-experiments#f4ec724d)。
![Image=2360x1400](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/00b5d6d5e0da4d32ae440754c3f2b969~tplv-goo7wpa0wc-image.image)
## 相关信息 {#18bb071f}
### 评测集数据类型 {#e9e3a87a}
创建评测集时，你需要为每个字段设置数据类型，扣子罗盘通过校验数据类型，避免导入数据不匹配的情况，保证评测的数据质量；同时可以提高数据的消费和存储成本。
目前扣子罗盘评测集支持以下常见类型的数据字段：
<!-- @cols-width: 107,389,500 -->
| | | | \
|**数据类型** |**说明** |**示例** |
|---|---|---|
| | | | \
|string |字符串，可用于存储任何数据类型。 |"helloworld" |
| | | | \
|int |整数，等同于 int64。 |1 |
| | | | \
|float |浮点数，等同于 float64。 |1.23 |
| | | | \
|boolean |布尔值。 |true |
| | | | \
|Object |对象数据类型，典型适用场景包括： |\
| | |\
| |* 评测对象有相对固定的 IDL（接口定义语言）。 |\
| |* 线上 Trace 回流时，需要确保流入评测集的数据的规整，避免数据污染。 |\
| |* 配置实验时，需要下钻到 Object 对象的某个内部字段。 | |\
| | |{ |\
| | |  "content": "hello world", |\
| | |  "user_name": "alice" |\
| | |} |\
| | | |\
| | | |
| | | | \
|Array |数组数据类型，数组内部的 Item 类型支持设置为： |\
| | |\
| |* String |\
| |* Int |\
| |* Float |\
| |* Boolean |\
| |* Object |[1,2,3,4,5] |
| | | | \
|多模态 |\
| |多模态数据类型，可以是图片、音频或视频，也可以是文字、图片、音频与视频的混合。 |\
| |多模态类型的字段固定为 Array<Object> 类型。参阅 [向评测集添加多模态数据](/cozeloop/multi-modal-dataset) 。 | |\
| | |[ |\
| | |  { |\
| | |    "type": "text", |\
| | |    "text": "What is in this image?" |\
| | |  }, |\
| | |  { |\
| | |    "type": "image_url", |\
| | |    "image_url": { |\
| | |      "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" |\
| | |    } |\
| | |  }， |\
| | |  { |\
| | |    "type": "audio_url", |\
| | |    "audio_url": { |\
| | |      "url": "https://example.com/audio" |\
| | |    } |\
| | |  }， |\
| | |  { |\
| | |    "type": "video_url", |\
| | |    "video_url": { |\
| | |      "url": "https://example.com/video" |\
| | |    } |\
| | |  } |\
| | |] |\
| | | |\
| | | |
| | | | \
|轨迹 |轨迹（Trajectory）数据类型。 |\
| |轨迹是指 AI Agent 在任务执行过程中生成的结构化时序数据，数据格式为 JSON。轨迹完整记录了从接收用户指令开始，Agent 在多轮交互中进行的思考、行动和观察的全链路历史。详情参见 [通过数据回流评测行程规划 Agent 的轨迹](/cozeloop/trajectory-evaluation-tutorial)。 |详情参见 [通过数据回流评测行程规划 Agent 的轨迹](/cozeloop/trajectory-evaluation-tutorial)。 |



