import 'package:flutter/material.dart';
import 'package:operahouse/screens/inputField1_Screen.dart';
import 'Button1_Screen.dart';
import 'inputField1_Screen.dart';

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
            Button()
          ],
        ),
      ),
    );
  }
}
