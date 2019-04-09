import java.math.BigInteger;

public class Lesson1_3 {
    /**
    * @Description: 二进制按位“或”的操作
    * @param num1- 第一个数字,num2- 第二个数字
    * @return 二进制按位“或”的结果
    */
    public static int or(int num1, int num2) {
		return (num1 | num2);
	}	

    /**
    * @Description: 二进制按位“与”的操作
    * @param num1- 第一个数字,num2- 第二个数字
    * @return 二进制按位“与”的结果
    */
	public static int and(int num1, int num2) {
		return (num1 & num2);
	}

    /**
    * @Description: 二进制按位“异或”的操作
    * @param num1- 第一个数字,num2- 第二个数字
    * @return 二进制按位“异或”的结果
    */
	public static int xor(int num1, int num2) {
		return (num1 ^ num2);
	}

    public static String decimalToBinary(int decimalSource) {
        BigInteger bi = new BigInteger(String.valueOf(decimalSource));
        return bi.toString(2); // 参数2指定的是转化成二进制
    }

    public static int binaryToDecimal(String binarySource) {
        BigInteger bi = new BigInteger(binarySource, 2);
        return Integer.parseInt(bi.toString());
    }

    public static void main(String[] args) {
        int a = 53;
        int b = 35;
        System.out.println(String.format("数字 %d(%s) 和数字 %d(%s)的按位‘或’的结果 %d(%s)", a, decimalToBinary(a),b, decimalToBinary(b),or(a,b),decimalToBinary(or(a,b))));
        System.out.println(String.format("数字 %d(%s) 和数字 %d(%s)的按位‘与’的结果 %d(%s)", a, decimalToBinary(a),b, decimalToBinary(b),and(a,b),decimalToBinary(and(a,b))));
        System.out.println(String.format("数字 %d(%s) 和数字 %d(%s)的按位‘异或’的结果 %d(%s)", a, decimalToBinary(a),b, decimalToBinary(b),xor(a,b),decimalToBinary(xor(a,b))));
    }
}
