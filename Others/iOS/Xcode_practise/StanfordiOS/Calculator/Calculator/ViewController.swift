//
//  ViewController.swift
//  Calculator
//
//  Created by 朱守亮 on 15/3/28.
//  Copyright (c) 2015年 sh. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var display: UILabel!

    var userIsInTheMiddleOfTypingANumber = false
    
    @IBAction func appendDigit(sender: UIButton) {
        let digit = sender.currentTitle!
        if userIsInTheMiddleOfTypingANumber{
            display.text = display.text! + digit
        } else{
            display.text = digit
            userIsInTheMiddleOfTypingANumber = true
        }
    }
    
    //计算func
    @IBAction func operate(sender: UIButton) {
        let operation = sender.currentTitle!
        if userIsInTheMiddleOfTypingANumber{
            enter()
        }
        switch operation{
            case "×":performOperation{  $0 * $1 } //函数闭包
            case "÷":performOperation{  $1 / $0 }
            case "+":performOperation{  $0 + $1 }
            case "−":performOperation{  $1 - $0 }
            case "√":performOperation{  sqrt($0)  }
            default: break
        }
    }
    
    //函数重载
    func performOperation(operation:(Double,Double) ->Double){
        if operandStack.count >= 2{
            displayValue = operation(operandStack.removeLast() ,operandStack.removeLast())
            enter()
        }
    }
    
    func performOperation(operation:Double ->Double){
        if operandStack.count >= 1{
            displayValue = operation(operandStack.removeLast())
            enter()
        }
    }
    
    var operandStack = Array<Double>()
        
    @IBAction func enter() {
        userIsInTheMiddleOfTypingANumber = false
        operandStack.append(displayValue)
        print("operandStack = \(operandStack)")
    }
    
    //计算属性
    var displayValue: Double{
        get{
            return NSNumberFormatter().numberFromString(display.text!)!.doubleValue
        }
        set{
            display.text = "\(newValue)" //必须为关键字newValue
            userIsInTheMiddleOfTypingANumber = false
        }
    }
    
}

