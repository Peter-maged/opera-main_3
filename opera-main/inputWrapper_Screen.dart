import 'package:flutter/material.dart';
import 'package:operahouse/screens/inputField_Screen.dart';
import 'Button_screen.dart';
import 'inputField_Screen.dart';

class InputWrapper extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(30.0),
      child: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            SizedBox(
              height: 40,
            ),
            Container(
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10.0),
              ),
              child: InputField(),
            ),
            SizedBox(
              height: 40,
            ),
            Text(
              "Forget Password",
              style: TextStyle(color: Colors.grey),
            ),
            SizedBox(
              height: 40,
            ),
            Button()
          ],
        ),
      ),
    );
  }
}
