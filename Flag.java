public class Flag {
    public static void main(String[] args) {
	int flag_a = 90;
	int flag_b = 101;
	int flag_c = 114;
	int flag_d = 111;
	int flag_e = 68;
	int flag_f = 97;
	int flag_g = 121;
	int flag_h = 115;
	int flag_i = 123;

	int[] flag_start = new int[]{
	    flag_a, flag_b, flag_c, flag_d,
	    flag_e, flag_f, flag_g, flag_h,
	    flag_i
	};

	int[] lolwut = new int[]{
	    57, 4, 20, 10, 38, 0, 27, 22, 6
	};

	int[] hide_me = new int[lolwut.length * 2];

	int j = 0;
	for (int i = 0; i < lolwut.length * 2; i++) {
	    if (i >= lolwut.length) {
		j = i - lolwut.length;
		hide_me[i] = lolwut[j] ^ flag_start[j]; 
	    }
	    else {
	    	hide_me[i] = flag_start[i];
	    }	    
	}
    }
}
