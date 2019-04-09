import java.math.BigInteger;

public class Lesson1_1 {
	/**
    * @Description: 十进制转换成二进制
    * @param decimalSource
    * @return String
    */
	public static String decimalToBinary(int decimalSource) {
		BigInteger bi = new BigInteger(String.valueOf(decimalSource));
		return bi.toString(2); // 参数2指定的是转化成二进制
	}

   /**
    * @Description: 二进制转换成十进制
    * @param binarySource
    * @return int
    */
	public static int binaryToDecimal(String binarySource) {
		BigInteger bi = new BigInteger(binarySource, 2);
		return Integer.parseInt(bi.toString());
	}

    public static void main(String[] args) {
        int a = 53;
        String b = "110101";
        System.out.println(String.format("数字 %d 的二进制是 %s", a, Lesson1_1.decimalToBinary(a)));
        System.out.println(String.format("数字 %s 的十进制是 %d", b, Lesson1_1.binaryToDecimal(b)));
    }
}
