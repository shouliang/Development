/**
 * Created by shouliang on 2016/5/11.
 */
/***
 * 策略模式的定义是： 定义一系列的算法，把它们一个个封装起来，并且使它们可以相互替换。
***/

// 使用策略模式计算奖金

// 最初的代码实现
var calculateBonus = function (performanceLevel, salary) {
    if (performanceLevel === 'S') {
        return salary * 4;
    }

    if (performanceLevel === 'A') {
        return salary * 3;
    }

    if (performanceLevel === 'B') {
        return salary * 2;
    }
}

console.log(calculateBonus('S', 10000));
console.log(calculateBonus('A', 6000));
console.log(calculateBonus('B', 8000));

/*
可以发现，这段代码十分简单，但是存在着显而易见的缺点。
 calculateBonus 函数比较庞大，包含了很多 if-else 语句，这些语句需要覆盖所有的逻辑
分支。
 calculateBonus 函数缺乏弹性，如果增加了一种新的绩效等级 C，或者想把绩效 S 的奖金
系数改为 5， 那我们必须深入 calculateBonus 函数的内部实现，这是违反开放封闭原则的。
 算法的复用性差，如果在程序的其他地方需要重用这些计算奖金的算法呢？我们的选择
只有复制和粘贴。
*/


// 改进1 使用组合函数重构代码 各种算法封装到一个个的小函数中
var performanceS = function (salary) {
    return salary * 4;
}

var performanceA = function (salary) {
    return salary * 3;
}

var performanceB = function (salary) {
    return salary * 2;
}

var calculateBonus = function (performanceLevel, salary) {
    if (performanceLevel === 'S') {
        return performanceS(salary);
    }

    if (performanceLevel === 'A') {
        return performanceA(salary);
    }

    if (performanceLevel === 'B') {
        return performanceB(salary);
    }
}

console.log(calculateBonus('S', 10000));
console.log(calculateBonus('A', 6000));
console.log(calculateBonus('B', 8000));


// 改进2 模仿传统面对对象语言的策略模式
// 定义各策略类及策略方法
var performanceS = function () {
};

performanceS.prototype.calculate = function (salary) {
    return salary * 4;
};

var performanceA = function () {
};

performanceA.prototype.calculate = function (salary) {
    return salary * 3;
};

var performanceB = function () {
};

performanceB.prototype.calculate = function (salary) {
    return salary * 2;
};

// 定义奖金类 (环境类)
var Bonus = function () {
    this.salary = null;   // 原始工资
    this.strategy = null; // 绩效等级对应的策略对象
};

Bonus.prototype.setSalary = function (salary) {
    this.salary = salary;
};

Bonus.prototype.setStrategy = function (strategy) {
    this.strategy = strategy;
}

Bonus.prototype.getBonus = function () {
    return this.strategy.calculate(this.salary); // 把计算奖金的操作委托给对应的策略对象
}

// 定义一个bonus的对象
var bonus = new Bonus();

bonus.setSalary(10000);
bonus.setStrategy(new performanceS());

console.log(bonus.getBonus());


// 改进3 JavaScript版本的策略模式
var strategis = {
    "S": function (salary) {
        return salary * 4;
    },
    "A": function (salary) {
        return salary * 3;
    },
    "B": function (salary) {
        return salary * 2;
    }
}

var calculateBonus = function (level, salary) {
    return strategis[level](salary);
}

console.log(calculateBonus('S',10000));
console.log(calculateBonus('A',6000));
console.log(calculateBonus('B',8000));

/*
策略模式指的是定义一系
列的算法，把它们一个个封装起来。将不变的部分和变化的部分隔开是每个设计模式的主题，策
略模式也不例外，策略模式的目的就是将算法的使用与算法的实现分离开来。
在这个例子里，算法的使用方式是不变的，都是根据某个算法取得计算后的奖金数额。而算
法的实现是各异和变化的，每种绩效对应着不同的计算规则。
一个基于策略模式的程序至少由两部分组成。第一个部分是一组策略类，策略类封装了具体
的算法，并负责具体的计算过程。 第二个部分是环境类 Context， Context 接受客户的请求，随后
把请求委托给某一个策略类。要做到这点，说明 环境类Context 中要维持对某个策略对象的引用。
*/

/*
通过使用策略模式重构代码，我们消除了原程序中大片的条件分支语句。所有跟计算奖金有
关的逻辑不再放在 Context 中，而是分布在各个策略对象中。 Context 并没有计算奖金的能力，而
是把这个职责委托给了某个策略对象。每个策略对象负责的算法已被各自封装在对象内部。当我
们对这些策略对象发出“计算奖金”的请求时，它们会返回各自不同的计算结果，这正是对象多
态性的体现，也是“它们可以相互替换”的目的。替换 Context 中当前保存的策略对象，便能执
行不同的算法来得到我们想要的结果。
*/