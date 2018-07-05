//
//  ViewController.swift
//  L02UsingImageView
//
//  Created by 朱守亮 on 15/3/27.
//  Copyright (c) 2015年 sh. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

  
    @IBOutlet weak var iv: UIImageView! //按ctrl键将控件绑定到viewController
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        iv.image = UIImage(named: "min1.jpg") //手动设置imageView的图片
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

