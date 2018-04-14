package com.example.bhushan.a5_3;

import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.content.Context;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import net.objecthunter.exp4j.*;

public class MainActivity extends AppCompatActivity {

    private Button button[] =new Button[10];
    private TextView input;
    private TextView output;
    private Button clear,add,sub,mul,div,equal,sin,cos,tan,dot,pi,sqrt;
    private Button brOpen,brClose;
    private Button memSave,memRecall,memClear;

    private SharedPreferences sharedPreferences;
    private SharedPreferences.Editor editor;
    private static final String MyPREFERNCES = "Myprefs";
    private static final String Key = "Key";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        sharedPreferences = getSharedPreferences(MyPREFERNCES,Context.MODE_PRIVATE);
        editor= sharedPreferences.edit();

        setButtons();
        setOnClickListeners();

    }
    private void setButtons()
    {
        button[0] = findViewById(R.id.button0);
        button[1] = findViewById(R.id.button1);
        button[2] = findViewById(R.id.button2);
        button[3] = findViewById(R.id.button3);
        button[4] = findViewById(R.id.button4);
        button[5] = findViewById(R.id.button5);
        button[6] = findViewById(R.id.button6);
        button[7] = findViewById(R.id.button7);
        button[8] = findViewById(R.id.button8);
        button[9] = findViewById(R.id.button9);

        input = findViewById(R.id.exp);
        output = findViewById(R.id.res);

        clear = findViewById(R.id.clr);

        add = findViewById(R.id.add);
        sub = findViewById(R.id.sub);
        mul = findViewById(R.id.mul);
        div = findViewById(R.id.div);

        equal = findViewById(R.id.equal);

        sin = findViewById(R.id.sin);
        cos = findViewById(R.id.cos);
        tan = findViewById(R.id.tan);

        dot = findViewById(R.id.dot);
        brOpen = findViewById(R.id.brOpen);
        brClose = findViewById(R.id.brClose);
        sqrt = findViewById(R.id.sqrt);
        pi = findViewById(R.id.pi);

        memSave = findViewById(R.id.memSave);
        memRecall = findViewById(R.id.menRecall);
        memClear = findViewById(R.id.menClear);

    }

    private void setOnClickListeners()
    {
        View.OnClickListener temp = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String text = ((Button) v).getText().toString();
                input.append(text);
            }
        };

        for(int i=0;i<10;i++)
        {
            button[i].setOnClickListener(temp);
        }

        clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText("");
                output.setText("");
            }
        });

        add.setOnClickListener(temp);
        sub.setOnClickListener(temp);
        mul.setOnClickListener(temp);
        div.setOnClickListener(temp);

        sin.setOnClickListener(temp);
        cos.setOnClickListener(temp);
        tan.setOnClickListener(temp);

        dot.setOnClickListener(temp);
        brOpen.setOnClickListener(temp);
        brClose.setOnClickListener(temp);
        sqrt.setOnClickListener(temp);

        equal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onEqual();
            }
        });

        pi.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.append(Double.toString(Math.PI));
            }
        });

        memSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String text=output.getText().toString();
                if(text!="") {
                    editor.putString(Key,text);
                    editor.commit();
                    Toast.makeText(getApplicationContext(),text+"Data Stored",Toast.LENGTH_SHORT).show();
                }
                else
                    Toast.makeText(getApplicationContext(),"Output Empty",Toast.LENGTH_SHORT).show();

            }
        });

        memRecall.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String txt="";
                if(sharedPreferences.getAll().containsKey(Key))
                    input.append(sharedPreferences.getString(Key,""));
                else
                    Toast.makeText(getApplicationContext(),"Nothing in memory",Toast.LENGTH_SHORT).show();
            }
        });

        memClear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                editor.remove(Key);
                editor.commit();
                Toast.makeText(getApplicationContext(),"Memory Cleared",Toast.LENGTH_SHORT).show();
            }
        });
        }


        private void onEqual()
        {
            try {
                String txt= input.getText().toString();
                Expression expression = new ExpressionBuilder(txt).build();

                double  result =  expression.evaluate();
                output.setText(String.format("%12f",result));

            }
            catch (Exception ex)
            {
                output.setText("Error");
            }

    }




}
