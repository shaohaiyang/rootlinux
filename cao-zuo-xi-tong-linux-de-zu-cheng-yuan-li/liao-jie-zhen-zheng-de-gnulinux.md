# 了解真正的GNU/Linux

## GNU、Linux、操作系统、发行版本的关系

![GNU_Linux关系](https://raw.githubusercontent.com/shaohaiyang/rootlinux/master/images/s1_1_gnu.png)

### GNU/Free的起源 
GNU计划，又称"革奴计划"，是由Richard Stallman在1983年9月27日公开发起的，并发表了《GNU宣言》等解释为何发起该计划的文章，因为他看不惯大公司把Unix的版权商业化，封闭化，唯利是图。做为一名伟大的程序员兼自由斗士，他希望能够创建一套完全自由开源的操作系统。其中一个理由就是要“<font color=red><b>重现当年软件界合作互助的团结精神</b></font>”。 为保证GNU软件可以自由地“使用、复制、修改和发布”，所有GNU软件都有遵循GNU通用公共许可证的协议（GNU General Public License，GPL）, 即“反版权”（或称Copyleft）概念。

> GNU计划具有浓烈的理想主义色彩，同时也是开源世界的火种起源，试想在那个金钱、版权至上，计算机还是稀罕物的年代，一般会编程的人尤其是像R.S，70年代的哈佛高材生又受聘于麻省理工学院（MIT）人工智能实验室工作近10年的大神肯定能赚的盆满钵满，但是R.S这样的勇士敢于追寻自由的境界，才有了后面孕育Linux的温床，又掀起了持续至今的开源自由的OpenSource大潮，这是多大伟大的理想。

1985年Richard Stallman又创立了自由软件基金会（Free Software Foundation，<font color=red><b>Free是自由、开源的意思，不是免费！</b></font>）来为GNU计划提供技术、法律以及财政支持。尽管GNU计划大部分时候是由个人自愿无偿贡献，但FSF有时还是会聘请程序员帮助编写。当GNU计划开始逐渐获得成功时，一些商业公司开始介入开发和技术支持。当中最著名的就是之后被Red Hat兼并的 Cygnus Solutions。

1990年，GNU计划已经开发出的软件包括了一个功能强大的文字编辑器Emacs（史上最极客的鸡爪编辑器） 。GCC（GNU Compiler Collection，GNU编译器集合），是一套由 GNU 开发的编程语言编译器。以及大部分UNIX系统的程序库和工具。唯一依然没有完成的重要组件就是操作系统的内核(称为HURD)。

> GCC的出现非常重要，因为在这之前，gcc编译器也是有版权的商用软件，正因为有了它，才有了后面的千千万万的程序员自由的使用GCC开源编译器来贡献各种C程序，包括伟大的Linux内核的编写和诞生。

### Linux横穿出世 
1991年Linus Torvalds用C和GCC编写出了与UNIX兼容的[Linux操作系统内核](LINUX_KERNEL.md)并在GPL条款下发布，弥补了GNU没有内核的遗憾。没想到Linux之后在网上被广泛流传，吸引了许多杰出的程序员和黑客参与了开发与修改。

> 这里有个小插曲可以证明并不是只有Linux Torvalds和Richard Stallman等几个伟大的程序员在战斗。

> 以前的软件流传因为网络也没有现在发达，加上有版权限制，基本都是靠磁带拷贝人工传递，代码集中回到版权方再分发，这样就造成了无论是时间上还是代码质量上参差不齐，甚至各成一派，如UNIX流传到伯克利大学成了BSD的起源一样，称之为大教堂的开发模式，但是GNU/Linux类似集市开发的模式，因为遵循GPL分享的契约精神，每个人都必须开源所有的代码。

> 但是大家要知道，30年前的带宽远没有现在的快，而且非常昂贵，于是Perl之父Larry_Wall（除了耳熟能详的Perl语言，其实patch这个程序也是他写的），编写并开源了patch程序，正因为有了patch小程序，再也不需要软件整体拷贝重新发送，只要diff生成差异化文件，尺寸变得很小，用patch就可以让程序员之间很方便的共享"补丁"，让源码同步变得非常简单、更加方便和及时，可以集数量众多的极客智慧共同改进一个产品，这也是体现了GNU伟大的开源奉献精神！

![Linux内核](https://raw.githubusercontent.com/shaohaiyang/rootlinux/master/images/s1_2_kernel.jpg)

### Linux和操作系统的关系 

Linux只是一个[Kernel 内核](LINUX_KERNEL.md)!!! ，Kernel内核是提供硬件驱动的抽象层、文件系统、多任务等功能的系统软件，它封装好更加安全方便的与硬件紧密结合打交道的各种接口，可以把它理解成汽车上联系各个组件的CAN BUS总线系统。特点如下：
* 负责底层的硬件驱动,如电源，CPU，内存，硬盘，网卡，音视频硬件，定时器，各种输入输出设备；
* 它是一个模块化的宏内核，设备驱动程序可以完全访问硬件，并在系统运行期间可直接装载或卸载。
* 除了提供硬件抽象层外，它还封装了一些对编程友好的系统调用，包括如文件系统，进程管理，内存管理，调度器，加密API，KVM内核级虚拟化，IPC进程间通信和调度；
* 一些内核级应用程序的高效调用，如lvs，iptables，VLAN，aoe/iscsi/nfs/samba/rdb等内核级应用

注意：<html><font color=red><b>Linux并不是一套完整的操作系统</b></font></html>。直到1992年Linux与其他GNU软件结合，完全自由的操作系统才正式诞生，该操作系统往往被称为“GNU/Linux”或简称Linux。


### 为什么需要发行版本 
因为在GNU自由开源的集市开发模式下，很多的组件都是各自发展的，这一方面展示了蓬勃的生命力，另一方面也给软件间的协作带来困扰，导致并不是所有软件版本越新越好。于是，有些集成厂商会设置固定的截止日期，然后以此基础上做了大量软件版本的兼容性测试、整合、bug修复、安全加固等工作，除此之外还具备了一些人们所期待的特性，如：

* Redhat偏重于安全，稳定，可靠，有3～6个月的发布节奏及3～10年的生命周期，商业测试覆盖率高；
* Debian/Ubuntu有特别好用且量大的apt软件仓库，更加人性化的交互体验和活跃的社区支持；
* ArchLinux有类似BSD ports的滚动升级的包管理机制，系统极简而且效率更高；
* SUSE有基于QT的更加易用的图形控制台体验及兼容Redhat软件的包管理，迁移风险和成本较低；
* LFS《Linux From Scratch》确切地说，它并不是一个真正的发行版本，它就像一份Linux DIY菜谱，可以从已存在的 Linux宿主系统作为建立新系统的环境，提供包括编译器、连接器、源码下载和 Shell 等创建新系统的必要工具，打造自己的Linux系统；
.......

GNU/Linux代码本身并不收费，但提供了可收费的技术支持，满足了大千世界各种需求，这就是现在百家争鸣的发行版本的来历。

下面列举一些古老的，但仍然充满活力的Linux发行版本：

<font color=red size=+1><b>Slackware</b></font> Linux操作系统由Patrick Volkerding创建于1992年，是现存最古老的Linux发行版。它最大的特色就是基于shell和原生的简单PKG包管理机制，保持了GNU的原汁原味。

<font color=red size=+1><b>Debian</b></font> GNU / Linux 首次公布于1993年。其创始人为Ian Murdock（创始人因为莫名的原因选择了自杀，至今仍然是个谜），他设想通过已有的数百位开发志愿者在业余时间创建一个完全非商业目的的发行版。它成为最大的Linux发行版，也可能是迄今为止最大的协同软件项目！它的变种Ubuntu在南非富翁的赞助下已经变成了最流行的发行版本之一。


<font color=red size=+1><b>openSUSE</b></font> 的开始可追溯到1992年，德国的四个Linux爱好者 – Roland Dyroff, Thomas Fehr, Hubert Mantel和 Burchard Steinbild – 共同推出的SuSE Linux操作系统下的一个项目（Software und System Entwicklung）。在初期，年轻的公司出售载有德国版Slackware Linux的软盘，但是不久在1996年5月SuSE Linux 从4.2版开始作为独立版本发布。


<font color=red size=+1><b>Redhat</b></font> 发行版本起源可追溯至1995年，它是由两个Linux梦想家 – Bob Young和 Marc Ewing（在红帽Linux的名字）共同创建推出。1997年，红帽公司推出了其革命性的RPM包管理方案及其他高级特性，这极大的促进了发行版急速上升和普及，超越Slackware Linux成为全球最广泛使用的Linux发行版。在随后几年中，红帽公司制定了标准，每6个月发行的时间表。