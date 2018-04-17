package com.example.bhushan.b3_iameetha;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.content.Context;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    String DIGITS="0123456789";
    String OPERATORS="+-*/";
    String num;
    TextView input;
    TextView res;
    List<String> exp;
    double result;
    double saved_mem;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViewById(R.id.button0).setOnClickListener(this);
        findViewById(R.id.button1).setOnClickListener(this);
        findViewById(R.id.button2).setOnClickListener(this);
        findViewById(R.id.button3).setOnClickListener(this);
        findViewById(R.id.button4).setOnClickListener(this);
        findViewById(R.id.button5).setOnClickListener(this);
        findViewById(R.id.button6).setOnClickListener(this);
        findViewById(R.id.button7).setOnClickListener(this);
        findViewById(R.id.button8).setOnClickListener(this);
        findViewById(R.id.button9).setOnClickListener(this);

        findViewById(R.id.buttonAdd).setOnClickListener(this);
        findViewById(R.id.buttonSub).setOnClickListener(this);
        findViewById(R.id.buttonDiv).setOnClickListener(this);
        findViewById(R.id.buttonMul).setOnClickListener(this);

        findViewById(R.id.buttonSin).setOnClickListener(this);
        findViewById(R.id.buttonCos).setOnClickListener(this);
        findViewById(R.id.buttonTan).setOnClickListener(this);

        findViewById(R.id.buttonDot).setOnClickListener(this);
        findViewById(R.id.buttonClear).setOnClickListener(this);
        findViewById(R.id.buttonEquals).setOnClickListener(this);

        findViewById(R.id.buttonMr).setOnClickListener(this);
        findViewById(R.id.buttonMs).setOnClickListener(this);
        findViewById(R.id.buttonMemClear).setOnClickListener(this);

        input=(TextView)findViewById(R.id.textViewInp);
        res=(TextView)findViewById(R.id.textViewRes);

        num="";
        exp=new ArrayList<>();
        result=0.0;
    }

    @Override
    public void onClick(View v) {
        String text =( (Button) v).getText().toString();

        if(!(text.equals("=")) && !(text.equals("MS")) && !(text.equals("MR")) && !(text.equals("MC")))
        {
            input.append(text);
        }
        if(text.equals("MS"))
        {
            if(!res.getText().toString().equals(""))
            {

                saved_mem=Double.parseDouble(res.getText().toString());
            }
            else
            {
                saved_mem=0;
            }
        }
        if(text.equals("MR"))
        {
            input.append(String.valueOf(saved_mem));
            exp.add(String.valueOf(saved_mem));
            //  num.concat(String.valueOf(saved_mem));
        }
        if(text.equals("MC"))
        {
            saved_mem=0;
        }



        if(DIGITS.contains(text) || text.equals("."))
        {
            if(num.equals("") && text.equals("."))
            {
                num=0+text;
            }
            else
            {
                num=num.concat(text);
            }

        }
        else if(OPERATORS.contains(text) || text.equals("SIN") || text.equals("COS") || text.equals("TAN"))
        {
            if(!text.equals("SIN") || !text.equals("COS") || !text.equals("TAN"))
            {
                if(!num.equals(""))
                {
                    exp.add(num);
                    num="";
                }
            }
            if(text.equals("-"))
            {
                if(exp.isEmpty())
                {
                    exp.add(String.valueOf(0));
                }
            }

            exp.add(text);
        }
        else if(text.equals("="))
        {
            if(!num.equals(""))
            {
                exp.add(num);
            }
            result=EvaluateExpression(exp);
            writetoFile("hello.txt",getApplicationContext());
            res.setText(String.valueOf(result));
        }
        else if(text.equals("C"))
        {
            res.setText("");
            input.setText("");
            result=0.0;
            num="";
            exp=new ArrayList<>();

        }

    }

    public double EvaluateExpression(List<String> expr)
    {
        int i;
        double temp;
        while(expr.contains("+") || expr.contains("-") || expr.contains("/") || expr.contains("*") || expr.contains("SIN") || expr.contains("COS") || expr.contains("TAN"))
        {
            if(expr.contains("SIN"))
            {
                i=expr.indexOf("SIN");
                temp=  Math.sin(Math.toRadians(Double.parseDouble(expr.get(i+1))));
                expr.set(i,String.valueOf(temp));
                expr.remove(i+1);
            }
            else if(expr.contains("COS"))
            {
                i=expr.indexOf("COS");
                temp=  Math.cos(Math.toRadians(Double.parseDouble(expr.get(i+1))));
                expr.set(i,String.valueOf(temp));
                expr.remove(i+1);
            }
            else if(expr.contains("TAN"))
            {
                i=expr.indexOf("TAN");
                temp=  Math.tan(Math.toRadians(Double.parseDouble(expr.get(i+1))));
                expr.set(i,String.valueOf(temp));
                expr.remove(i+1);
            }

            else if(expr.contains("*"))
            {
                i=expr.indexOf("*");
                temp= Double.parseDouble(expr.get(i-1)) * Double.parseDouble(expr.get(i+1));
                expr.set(i,String.valueOf(temp));
                expr.remove(i-1);
                expr.remove(i);
            }
            else if(expr.contains("/"))
            {
                i=expr.indexOf("/");
                temp= Double.parseDouble(expr.get(i-1)) / Double.parseDouble(expr.get(i+1));
                expr.set(i,String.valueOf(temp));
                expr.remove(i-1);
                expr.remove(i);
            }
            else if(expr.contains("-"))
            {
                i=expr.indexOf("-");
                temp= Double.parseDouble(expr.get(i-1)) - Double.parseDouble(expr.get(i+1));
                expr.set(i,String.valueOf(temp));
                expr.remove(i-1);
                expr.remove(i);
            }
            else if(expr.contains("+"))
            {
                i=expr.indexOf("+");
                temp= Double.parseDouble(expr.get(i-1)) + Double.parseDouble(expr.get(i+1));
                expr.set(i,String.valueOf(temp));
                expr.remove(i-1);
                expr.remove(i);
            }

        }
        result=Double.parseDouble(expr.get(0));
        return result;
    }
    public void writetoFile(String xyz,Context context)
    {
        try
        {
            OutputStreamWriter s=new OutputStreamWriter(context.openFileOutput(xyz, Context.MODE_PRIVATE));
            s.write("\nResult="+Double.toString(result));
            s.close();
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }

    }
}