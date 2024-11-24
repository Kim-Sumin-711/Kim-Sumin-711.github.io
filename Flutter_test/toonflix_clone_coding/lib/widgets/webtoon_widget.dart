import 'package:flutter/material.dart';
import 'package:toonflix_clone_coding/screens/detail_screen.dart';

class Webtoon extends StatelessWidget {
  final String title, thumb, id;
  const Webtoon({
    super.key,
    required this.title,
    required this.thumb,
    required this.id,
  });

  @override
  Widget build(BuildContext context) {
    //detect user's gesture
    return GestureDetector(
      //onTap = onTapUp + onTap_down --> user clicks a button
      onTap: () {
        //route == statelesswidget+animation --> like another screen
        //in fact, render other statelesswidget.
        Navigator.push(
          context,
          //MaterialPageRoute is dependent to flatform.
          //alternative : use PageRouteBuilder
          MaterialPageRoute(
            builder: (context) => DetailScreen(
              title: title,
              thumb: thumb,
              id: id,
            ),
            fullscreenDialog: true,
          ),
        );
      },
      child: Column(
        children: [
          //Hero need tag.
          //Like original img moved to the center.
          Hero(
            tag: id,
            child: Container(
              width: 200,
              clipBehavior: Clip.hardEdge,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                boxShadow: [
                  BoxShadow(
                    blurRadius: 10,
                    offset: const Offset(10, 10),
                    color: Colors.black.withOpacity(0.4),
                  ),
                ],
              ),
              height: 250,
              //https://kmkn.tistory.com/22
              //object progressevent Error
              //or vsc setting --> web renderer --> html
              child: Image.network(thumb),
            ),
          ),
          const SizedBox(
            height: 10,
          ),
          Text(
            title,
            style: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }
}
