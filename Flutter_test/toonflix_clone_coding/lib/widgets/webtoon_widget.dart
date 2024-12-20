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
          PageRouteBuilder(
            transitionsBuilder:
                // secondaryAnimation: 화면 전화시 사용되는 보조 애니메이션효과
                // child: 화면이 전환되는 동안 표시할 위젯을 의미(즉, 전환 이후 표시될 위젯 정보를 의미)
                (context, animation, secondaryAnimation, child) {
              // Offset에서 x값 1은 오른쪽 끝 y값 1은 아래쪽 끝을 의미한다.
              // 애니메이션이 시작할 포인트 위치를 의미한다.
              var begin = const Offset(1.0, 0);
              var end = Offset.zero;
              // Curves.ease: 애니메이션이 부드럽게 동작하도록 명령
              var curve = Curves.ease;
              // 애니메이션의 시작과 끝을 담당한다.
              var tween = Tween(
                begin: begin,
                end: end,
              ).chain(
                CurveTween(
                  curve: curve,
                ),
              );
              return SlideTransition(
                position: animation.drive(tween),
                child: child,
              );
            },
            // 함수를 통해 Widget을 pageBuilder에 맞는 형태로 반환하게 해야한다.
            pageBuilder: (context, animation, secondaryAnimation) =>
                // (DetailScreen은 Stateless나 Stateful 위젯으로된 화면임)
                DetailScreen(title: title, thumb: thumb, id: id),
            // 이것을 true로 하면 dialog로 취급한다.
            // 기본값은 false
            fullscreenDialog: false,
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
