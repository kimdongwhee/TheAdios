import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("프로젝트 활용 데이터관련 EDA((Exploratory Data Analysis)")
st.subheader(":one: 24년도 축구선수 데이터")
st.markdown(":white_check_mark: 데이터 소개 : 국가별 축구 팀 소속의 스카우터들이 축구선수에 대한 속성을 수치화한 데이터임.\n(속성 분류 : Technical, Mental, Physical, GOALKEEPING)")
st.markdown(":white_check_mark: 데이터 출처 : FM Inside(https://fminside.net/)")
st.markdown(":white_check_mark: 데이터 활용계획")
st.text("- 유망주 예측\n- 선수별 잠재력 예측\n- 포지션별 유사선수 클러스터링\n- 랭체인기반 챗봇(선수정보 등)")

st.markdown(f":white_check_mark: 데이터 세부내용")

tab1, tab2, tab3, tab4 = st.tabs(['Technical', 'Mental', 'Physical', 'GOALKEEPING'])

with tab1:
    st.text('''
    (1) 개인기(Technique): 공을 가지고 있을 때 기술적인 면에서 얼마나 화려한 플레이를 할 수 있는지를 나타낸다. 까다로운 패스나 크로스, 슈팅을 잘하기 위해 중요한 능력이다. 개인기가 높은 선수는 까다로운 패스나 경기장을 가로지르는 패스를 더 손쉽게 성공시킨다. 또한 다른 기술적 능력과도 관계가 있어, 낮은 개인기를 가진 선수는 다른 기술적 능력도 전반적으로 낮아진다. 개인기라는 이름 때문에 오해를 자주 사는데, 공을 가지고 있을 때의 발재간은 기술적 능력 중에서는 오직 드리블 능력치만이 직접적으로 작용한다. 개인기는 주로 공이 선수의 발을 떠나는 순간에 작용하는 능력치다.\n
    (2) 골 결정력(Finishing): 기회가 났을 때 골 네트를 흔들 수 있는 선수의 능력. 골 결정력 능력치가 높으면 최소한 골대 안으로 슛을 쏘며, 능력치가 낮은 선수에 비해 골키퍼가 막을 수 없는 곳으로 공을 보낼 것이다. 이것은 순수하게 슛의 정확도를 결정하는 능력이며, 꾸준히 득점하려면 침착성과 판단력 능력도 중요하다. 인플레이 상황에서 페널티 박스 안에서 슈팅하는 상황에 적용되는 능력치다. 실험에 따르면 1~13까지는 큰 차이가 없으나 15부터는 능력치가 상승할 때마다 뚜렷한 차이를 보인다. 20과 13를 비교하면 엄청난 차이가 나타났다. 단순히 득점만을 원한다면 침착성보다는 골 결정력이 높은 선수가 효율적이다.\n
    (3) 드리블(Dribbling): 공을 가지고 얼마나 잘 달릴 수 있는지, 뺏기지 않고 얼마나 잘 관리하는지 나타낸다. 이 능력은 선수가 순전히 발로 공을 다루는 실력을 뜻하며, 주력과 가속도, 민첩성, 균형감각이 다양한 상황에서 드리블 능력에 영향을 준다. 즉, 드리블 능력치가 높다면 다양한 상황에서 유용하게 쓰이기는 해도 그것만으로는 부족하다.\n
    (4) 일대일 마크(Marking): 수비 시 상대 선수를 얼마나 잘 마크하는지 보여주는 능력치. 이 능력치가 낮다면 대인마크 시에 마크해야 할 선수를 프리상태로 두는 확률이 높아진다. 몸싸움, 수비 위치 선정, 예측력과 관련이 있다. 그 외에도 두 선수의 신체적 차이가 영향을 준다.\n
    (5) 장거리 스로인(Long Throws): 스로인을 얼마나 멀리 던지는가 보여주는 능력치. 주로 공격 상황에서 발휘한다. 이 능력치가 일정 이상이고 선플로 장거리 스로인이 붙어있으면 적 진영에서의 스로인 상황시 매우 유용하다. 주로 좌우 풀백이 높은 편이다.\n
    (6) 중거리 슛(Long Shots): 페널티 박스 바깥에서의 슛 정확도를 나타내는 능력치. 의외로 골 결정력과는 별 관계없다. 직접 프리킥을 찰 때 중요하다. 페널티 에어리어 바깥에서 감아찰 기회가 자주 나오는 측면 공격형 미드필더나 공격적인 롤을 맡은 2/3선 중앙 미드필더에게 요구된다. 다른 능력치들과 상당히 독립된 능력치이며 선호하는 플레이와 잘 조합하는 것이 중요하다.\n
    (7) 코너킥(Corners): 정확하게 코너킥을 찰 수 있는 능력. 코너킥 능력치가 높으면 이따금 코너킥으로 골을 넣는 진기명기를 보여주기도 한다.\n
    (8) 크로스(Crossing): 측면에서 페널티 박스로 공을 크로스 할 때의 정확도를 보여주는 능력치. 높을수록 좋은 득점 기회를 만들어 낸다. 코너킥/프리킥 상황에서도 영향을 준다고 알려져 있다. 풀백과 윙어에게 요구된다.\n
    (9) 태클(Tackling): 수치가 높다면 드리블 수치가 높은 선수 상대로 태클을 성공할 확률이 높아지고 반칙을 범할 확률이 낮아진다.\n
    (10) 패스(Passing): 패스의 정확도를 보여주는 능력치. 이 능력치와 개인기가 높으면 장거리 패스도 정확히 할 수 있다.\n
    (11) 퍼스트 터치(First Touch): 공을 받은 후 다음 동작으로의 연결에 영향을 끼친다. 낮으면 터치가 길어 볼을 놓칠 수 있고 능력치가 높으면 원터치로 골을 넣는 등의 효과가 있다.\n
    (12) 페널티킥(Penalty Taking): 선수의 페널티킥 능력. 높을 수록 정확도가 높아진다. 침착성도 페널티 성공 여부와 상관있지만 페널티킥 능력치 자체가 페널티킥의 득점 여부를 좌우한다. 페널티킥 상황에서 골 결정력은 적용되지 않는다. 물론 페널티킥이 상대 골키퍼의 펀칭으로 막혔을 때 세컨 볼을 처리하려면 골 결정력이 필요할 수도 있다. 골키퍼의 페널티킥을 막아내는 능력은 처음에는 예측력, 반사 신경, 공을 차는 순간에 반응하는 집중력에 의해 결정된다. 순간 속도는 공을 곧바로 잡을 수 있도록 도움을 주며, 민첩성, 반사 신경, 볼 핸들링은 최종적으로 선방이 성공할 지 결정한다.\n
    (13) 프리킥(Free Kick Taking): 프리킥을 얼마나 잘 차는지 보여주는 능력치. 직접 슈팅으로 골을 넣을 때에만 적용된다. 간접 프리킥은 크로스 같은 다른 기술적 능력에 의해 통제된다. 많은 선수가 높은 프리킥 능력을 가질 필요는 없으나 뛰어난 프리키커 한두 명이 있으면 팀 전체의 득점력을 높이는데 큰 도움이 된다. 측면에서 크로스하는 위치(wide crossing positions)에서의 프리킥의 경우 실제로는 취하는 행동에 따라 코너킥이나 패스가 사용된다. 예를 들어, 코너 플래그 근처에서 프리킥의 경우 같은 종류의 기술이 요구되기 때문에 코너킥 능력치가 사용된다. 개인기의 경우 선수가 공에 얼마나 많이 회전을 줄 수 있는지를 결정하는데 사용되므로 유용하다. FM23까지는 '골 결정력'과 '중거리 슛'이 영향을 미치지 않았으나, FM24부터는 게임 메뉴얼의 능력치 설명에 중거리슛의 영향을 받는다는 내용이 추가되었다.\n
    (14) 헤더(Heading): 헤더의 정확도를 결정하는 능력. 점프 거리가 선수의 헤더 능력과 관련이 많으며 몸싸움, 대담성 또한 약간의 비중을 차지한다.''')

with tab2:
    st.text('''
    (1) 대담성(Bravery): 위험한 플레이에 대한 선호도를 나타내며 헤더에 연계돼서 매우 중요한 능력치다. 점핑리치와 헤더 능력치가 높아도 대담성이 낮으면 공중볼 경합을 피해서 헤더 빈도가 줄어들게 된다. 선호하는 플레이가 없던 예전 버전에는 드리블 돌파 회수에도 관련된 능력치였지만, 선플이 생기고 나서는 그 부분은 삭제 된 듯 하다. 대부분의 장기 부상은 이 능력치가 주로 하락하지만[62] 드물게 다시 회복되기도 한다.\n
    (2) 리더십(Leadership): 다른 선수들에게 영향을 미칠 수 있는지 나타내는 능력치. 리더쉽이 높은 선수가 주장이 선수단 분위기나 화합도, 혹은 경기 중에도 영향을 준다. 불만을 가진 선수도 감독 대신 설득이 가능하기 때문에 팀에 한두 명 정도 리더쉽이 높은 선수가 있는 것이 좋다.\n
    (3) 승부욕(Determination): 승부욕은 성공하기 위한 헌신을 뜻한다. 승부욕이 있는 선수는 승리하기 위해 온 힘을 다한다. 이 능력은 대담성과 연관이 있다. 두 능력은 서로 뗄 수 없는 관계이므로 둘 중의 하나가 높은 선수는 다른 하나도 높을 수 있다. 모든 포지션, 전연령대에서 어빌에 영향 주지 않는다. 경기를 이기기 위한 욕구를 나타낸 능력치이므로 이 능력치가 높으면 그만큼 골을 많이 넣게 되거나 역전골을 잘 넣게 된다.. 또한 지고 있는 상황에서 분발해서 플레이할 수 있게 해준다. 경기 후 평점이 낮을 경우 경고를 먹이면 랜덤 확률로 16까지 오르고 16 이후에 벌금을 먹이면 추가적으로 오른다. 리그나 챔스 득점왕들이 이 능력치가 높다. 수비수나 골키퍼 중에서도 월드클래스급 선수들은 이 능력치가 높은 경우가 많다. 왜냐하면 상대 공격수가 골 넣는 것을 막아야 경기에 이길 수 있게 되니까. 골에 대해 직접적으로 관여하는 바가 적은 미드필더나 윙백 같은 경우 플레이 스타일에 따라 대담성이나 적극성은 높아도 이 능력치는 비교적 낮은 경우가 많다. 어린 나이의 유망주가 고연봉을 받을 경우 승부욕이 급하락하는 경우도 있다.\n
    (4) 시야(Vision): 원거리의 아군을 찾아내는 능력. 전술적으로 아군을 이용할 수 있는지와는 관계가 없다. 시야 능력치 높은 선수가 원거리의 아군을 발견해도 기술적인 역량이 없으면 이를 이용할 수 없다. 이 능력은 선수가 원거리의 상황을 포착할 가능성을 좌우하며, 수치가 높은 경우 멀리 떨어진 곳의 아군을 잘 찾아낸다.\n
    (5) 예측력(Anticipation): 공의 움직임을 미리 예측해서 움직이는 능력치. 이 능력이 높은 선수는 경기의 흐름을 잘 파악하며 다른 선수보다 빨리 상황에 대처할 수 있다. 이 능력은 오프 더 볼과 잘 어울린다. 인자기 같은 포처나 수비수, 골키퍼들이 이 능력치가 높다.\n
    (6) 오프 더 볼(Off the ball): 공을 갖지 않을 때의 움직임. 예상대로, 이것은 오프 더 볼 상황에서, 특히 공격형 선수들이 상황을 판단하고 마킹을 피하거나, 스스로 패스를 한 후 다른 행동을 할 수 있게 하거나 팀 동료로부터 공을 받을 수 있는 위치로 이동할 수 있게 한다.\n
    (7) 위치 선정(Positioning): 선수가 상황을 읽고 데드볼 상황에서 벌어지는 일을 처리할 수 있는 가장 좋은 위치로 이동할 수 있는 능력. 골키퍼의 경우에는 전술에 따른 정확한 포지션에 얼마나 잘 위치해 있는가를 나타낸다. 공격 상황에서는 세트피스 시의 위치선정에 적용된다. 만약 이 능력치가 낮다면 아무리 점핑리치가 높고 헤더 능력이 좋아도 공의 착지 지점을 잘못 잡아서 공중볼을 놓치게 되고 상대 선수에게 역습을 허용하는 계기를 만들어 줄 수도 있다. 크로스나 로빙 스루 패스 처럼 낮고 빠르게 날라오는 공에 대해서는 이 능력치가 적용되지 않는다. 땅볼로 굴러오는 패스는 숏패스, 공중으로 날라오는 패스는 롱패스로 부르는 것과 달리 축구에서는 공중으로 날라오는 크로스나 땅위로 굴러오는 크로스도 다 크로스라 부르며, 이런 측면에서 빠르게 올라오는 공을 캐치하기 위해선 오프더볼과 예측력 능력치가 작용된다.\n
    (8) 적극성(Aggression): 상대 선수에 대한 태클의 강도나 빈도등을 나타낸다. 당연히 일반적으로 수비수들은 높지만 공격수들은 낮은 능력치. 단 루니나 즐라탄 처럼 상대 선수에게 거친 태클이나 보복성 태클을 좋아하는 공격수들은 이 능력치가 높다. 박지성 처럼 수비는 열심히 해도 거친 태클을 하지 않는 선수들은 이 능력차가 낮다. 그렇다고 해서 꼭 더티 플레이를 나타내는 지표는 아니다. 너무 높으면 카드를 쉽게 받고 너무 낮으면 태클 빈도가 낮아지는 능력치. 공격의 적극성으로 오인, 오버래핑에 관여하는 능력치로 착각하는 사람들도 있다. 어빌에 영향을 주지 않는 능력치다.\n
    (9) 집중력(Concentration): 매 경기의 모든 일에 주의를 기울이고 정신적으로 집중하는 선수의 능력을 나타낸다. 이 등급이 높은 선수는 일정이 진행되는 동안 집중력을 오래 유지할 수 있으며, 체력이 떨어진 후반에도 전반의 상황처럼 날카롭게 반응할 수 있다. 집중력이 낮은 선수는 집중력을 잃어서 경기의 중요한 순간에 실수할 수 있다. 수비 시 상대 공격수의 오프사이드 트랩이나 화려한 개인기에 속지 않고 집중하여 수비를 할 수 있게 만든다. 또한 드로잉 처럼 플레이가 일시 정지 된 상태에서 멍 때리지 않고 상대의 공격을 계속 표적해서 쫓아 가게 할 수 있는 능력. 공격수나 미드필더가 이 능력치가 높으면 전체적인 플레이 속도가 빨라져 슛 빈도나 패스 빈도가 높아지게 된다.\n
    (10) 천재성(Flair): 천재성 능력치가 높은 선수는 어떤 팀에서도 공격의 핵심 요소로 쓰이지만, 능력을 최대한 발휘하게 하려면 전술적인 통제가 필요하다. 개인기 시도, 킬러볼, 기회창출 무브먼트의 빈도를 나타낸 능력치. 이른바 크랙들에게는 매우 중요한 능력치지만 후방 빌드업 비중이 높지않은 팀의 수비수나 전술적 엄격함을 추구하는 팀에게는 중요하지 않은 능력치다. 박투박이나 홀딩처럼 안정성이 중시되는 포지션에겐 이 수치가 높다면 오히려 독이 되기도 하며, 공격수들 중에서도 플레이메이커나 메짤라 한두명 정도만 제하고 모든 선수가 이 능력을 갖출 필요는 없다. 때문에 공격수더라도 주력, 크로스 위주의 윙어나 타겟맨, 치달형 포처나 근거리 티키타카 볼배급을 하는 미들에겐 큰 의미가 없는 능력치. 기행 능력치가 없던 구버전에서는 특이한 플레이를 자주하는 골키퍼들의 경우 이 능력치가 높았다. 어빌에 영향을 주지 않는 능력치다.\n
    (11) 침착성(Composure): 침착성은 특히 공에 관한 선수의 마음과 능력의 안정성을 나타낸다. 골을 넣을 좋은 기회나 무거운 수비 부담을 마주했을 때, 침착성이 높은 선수는 정신을 똑바로 차리고 대개 팀에 도움이 되는 현명한 선택을 해낸다. 부족한 공격수들은 압박감에 시달리기 쉬우며, 일대일 득점찬스에서 골을 놓치기 쉽다. 실험에 따르면 득점력에서는 1과 13에는 엄청난 차이가 나타났지만 13과 20에는 별다른 차이가 없었다. 그러므로 단순히 득점을 원한다면 침착성 13정도에 골결정력이 높은 선수가 훨씬 더 효율적이다.\n
    (12) 팀워크(Teamwork): 주로 전술적 지시를 따라 팀 동료와 협력할 수 있는 선수의 능력을 나타낸다. 이 등급이 높은 선수로 이뤄진 팀은 한 집단으로서 잘 작동한다. 이 등급이 낮은 선수는 게으름을 피우며 팀 스피릿을 믿는 않는다. 아무리 능력치가 좋은 선수라 하더라도 팀워크가 낮으면 팀원의 프리 찬스를 무시하고 혼자 드리블 하다가 홈런을 치는 경우가 많다.(탐욕왕) 또한 선수가 전술 지침에 앞서 선플 중 하나를 사용할지 여부를 결정하는 데에도 사용된다.\n
    (13) 판단력(Decisions): 공이 있을 때나 없을 때 상황을 잘 판단하여 옳은 결정을 내리는 능력. 이 속성은 모든 포지션에서 중요하며, 평정심과 협력하여 선수가 주어진 순간에 얼마나 압박감을 느낄지 결정하고 그에 따라 최선의 선택을 한다. 토마스 뮐러나 세르히오 부스케츠같은 축구 지능이 높은 선수들이 높게 책정받은 능력치인데, 순간 속도와 주력 다음으로 어빌을 많이 잡아먹는 능력치인 반면에 체감은 크게 좋지 않아 이른바 분배가 좋은 선수들은 이 능력치가 낮은 경우가 많다.\n
    (14) 활동량(Work Rate): 선수가 최대 한계까지 노력하려는 정신적 추진력을 반영한다. 높은 등급의 선수는 처음부터 끝까지 열심히 노력하고 싶어하지만 실제 결과를 보이기 위해서는 좋은 신체적 특성[74]이 필요하다. 그게 아니더라도 팀에 도움이 되는 특성은 맞다. 말하자면 쓸데없이 뛰어다니기만 하는 게 아니라 자신의 임무를 뛰어넘어 경기를 수행하려는 의지다. 승부욕과 마찬가지로 평점이 낮을 경우 경고를 먹이면 랜덤확률로 16까지 오르며 16 이후에 벌금을 먹이면 추가적으로 성장시킬 수 있다. 단, 활동량은 승부욕과는 달리 어빌을 소모하므로 고의로 성장시킬 경우 타 능력치가 감소하는 스탯 조정이 발생한다. 때문에 유망주가 아니라면 승부욕 16을 찍은 후 부진했을 때에는 벌금을 먹이는 편이 낫다.''')

with tab3:
    st.text('''
    (1) 가속도(Acceleration): 정지 상태에서 순간적으로 치고 나갈 때 얼마나 최고 속력에 빠르게 도달하는지 나타내는 능력치. 당연하게도 주력과 긴밀한 연관성을 가진다. 매치 엔진의 특성상 주력과 함께 가장 중요한 능력치로 꼽히고 어빌을 가장 많이 잡아먹는 능력치다..\n
    (2) 균형감각(Balance): 드리블 시 상대방의 태클을 받았을 때나 급격한 방향전환을 할 때 넘어지지 않고 버틸 수 있게 만드는 능력치. 방향 전환 뿐만 아니라 점프 상태에서 아크로바틱한 동작(헤더, 시저스, 발리 등)에 작용하며, 신체 경합 상황에서 몸싸움 수치와 함께 적용되어 헤딩 경합하는 센터백이나 수비형 미드필더, 몸으로 비비는 타겟맨의 움직임에 영향을 미친다..\n
    (3) 몸싸움(Strength): 상대방에게 물리적인 힘을 발휘하여 우위를 점하는 능력. 몸싸움 상황, 공중볼 경합 등의 선수간 신체 접촉이 있는 모든 상황에 관여한다..\n
    (4) 민첩성(Agility): 선수가 다양한 속도에서 얼마나 잘 움직임을 시작하는지, 멈추는지, 다른 방향으로 전환하는지를 나타내는 수치. 매치 엔진에서는 주력, 가속도, 균형 감각과 연계되어 있으며 특히 한 번의 행동 이후 다음 동작까지의 텀을 결정한다. 대체로 키가 작을수록 수치가 높고 키가 클 경우 낮은 편이며, 잔발 동작, 세밀한 볼 터치에 영향을 준다..\n
    (5) 점프 거리(Jumping Reach): 선수가 공중에 있는 공을 처리하기 위해 점프했을 때 도달할 수 있는 최고 높이를 의미한다. '점프력'으로 번역되어 왔기 때문에 오해를 많이 사는 능력치인데, 점프 거리가 동일한 두 선수의 경우 키가 차이나더라도 인게임에서는 같은 거리로 점프한다. 공중볼을 처리하는 데에 있어서는 헤더, 대담성, 몸싸움 능력치가 함께 연관한다..\n
    (6) 주력(Pace): 선수의 최고 속도를 나타낸다. 가속도는 최고 속도에 얼마나 빨리 도달하는지 나타내며, 주력은 그 최고 속도를 뜻한다. 선수가 짧은 순간 또는 경기 전체에서 주력을 얼마나 오래 유지할 수 있는지는 지구력과 타고난 체력에 영향을 받는다. 물론, 공을 갖고 있을 때는 그렇지 않을 때보다 조금 느려진다..\n
    (7) 지구력(Stamina): 한 경기 내에서 체력을 유지하는 정도를 의미한다. 지구력이 높은 선수일수록 선수가 가진 최고의 퍼포먼스를 경기 내내 보여줄 수 있다. 지구력이 약한 선수는 더 빨리 지치게 되고, 지친 선수는 모든 플레이 단계에서 점점 더 임무 수행의 질이 떨어진다. 또한 타고난 체력과 직접 연관되어 있다.\n
    (8) 타고난 체력(Natural Fitness): 선수의 선천적인 체력. 휴식 중 체력 회복 및 에이징 커브와 관련된 능력치. 이 능력치가 높은 선수는 낮은 선수에 비해 경기와 경기 사이에 체력을 더 빠르게 회복하며 나이가 들어도 능력의 하락이 비교적 더 완만하다. 개별 훈련을 통해 성장시킬 수 없는 선천적이고 커리어 내내 거의 고정되어 있는 능력치다. 이 능력치가 낮은 선수는 판매 시기를 일찍 잡는 것이 좋다.''')

with tab4:
    st.text('''
    (1) 1:1 방어(One On Ones): 침착성, 수비 위치 선정 요구, 말 그대로 공격수와의 일대일 위기 상황에서 얼마나 침착하게 위치를 잘 잡아 대처하는지 보여주는 능력치\n
    (2) 골킥(Kicking): 골킥을 얼마나 빠르게, 멀리 차는지 보여주는 능력치. 원문이 Kicking인 만큼 정지된 공을 차는 것 뿐만 아니라 골키퍼가 차는 모든 롱킥의 능력치에 영향을 준다. 운이 좋으면 골킥으로 득점하는 경우도 있다.\n
    (3) 공 던지기(Throwing): 공을 얼마나 빠르게 정확하게 멀리 던지는지 보여주는 능력치. 이 등급이 높으면 던지기의 정확도가 상승하고, 던지기 거리는 몸싸움 능력치에 좌우된다. 크게 필요 하진 않고 10정도만 돼도 큰 불편이 없다. 그렇다고 너무 낮으면 압박수비하는 상대 공격수에게 실수로 뺏겨버리니 어느정도 훈련은 필요하다.\n
    (4) 공중 장악력(Aerial Reach): 높은 점프력, 볼 핸들링, 수비 위치 선정이 요구된다. 높은 크로스, 코너킥 처리를 쉽게 할수 있다. 공중볼을 처리해야 하는 상황에서 골키퍼의 신체적 역량을 나타냅니다. 키 큰 골키퍼는 선천적으로 키 작은 골키퍼가 닿지 못하는 높이에 닿을 수 있어 보통 이 등급이 높지만, 예외도 있습니다. 이 능력은 다른 골키퍼 관련 능력과 연계해서 골키퍼가 경기에서 공중 상황을 얼마나 잘 처리하는지를 결정한다.\n
    (5) 기행(Eccentricity): 골키퍼가 예상치 못한 행동을 할 가능성을 나타내며 일반적으로 골키퍼와는 완전히 다르게 행동할 가능성을 나타낸다. 기행이 높으면 골키퍼가 필드 플레이 상황에 가담할 확률이 높아진다. 예를들어 공을 몰고 나오거나 팀이 지고 있을 때 세트피스에 참여한다. 또한 높은 골키퍼는 드리블하며 자기 구역 밖으로 나오는 일이 흔하다.\n
    (6) 돌진(빈도)(Rushing Out): 골키퍼가 스루패스나 기타 유사한 상황에 반응해 얼마나 잘 뛰쳐나올 수 있는지를 나타낸다. 높은 주력과 가속도 능력을 가진 골키퍼는 돌진 능력이 더 뛰어나다.\n
    (7) 반사 신경(Reflexes): 반사 신경과 관련되며 선방에 큰 영향을 준다.\n
    (8) 볼 핸들링(Handling): 골키퍼에게 가장 중요한 능력치. 이 능력치가 높을수록 공중볼 장악때 실수가 줄어들고, 빠른 강슛도 쉽게 잡을수 있다. 골키퍼가 골을 막거나 루스 볼을 잡을 때 얼마나 안전하게 잡는지를 나타낸다. 볼 핸들링이 높으면 날씨가 나쁠 때 유용하지만, 보통 때도 공을 끈기 있게 잡아내는 골키퍼는 도움이 된다.\n
    (9) 수비 조율(Communication): 리더십, 판단력 요구, 수비진을 효과적으로 조율해 팀 전체 수비력을 강화시킨다. 수비진과 의사소통하여 팀의 수비 측면을 정비하는 골키퍼의 능력을 나타낸다. 등급이 높은 골키퍼는 의사소통을 더 잘하며 수비수끼리 효과적으로 연계하게 하여 전반적인 안정성을 높인다.\n
    (10) 펀칭(빈도)(Tendency To Punch): 펀칭 빈도는 골키퍼가 가능하면 공을 잡으려 하는지 아니면 펀칭으로 걷어내는 걸 선호하는지 나타낸다. 이 등급이 높으면 골키퍼가 공을 잡을 수 있을 때도 펀칭으로 걷어낸다는 뜻. 장단점이 있는 능력치. 높을수록 상대 슈팅을 쉽게 막지만 펀칭 후 루즈볼에 실점할 가능성이 높아지며, 낮으면 펀칭을 거의 안 하고 공을 잡으려고 시도해 루즈볼 기회를 주지 않지만 역효과로 상대 슈팅을 못 막게 될 수 있다. 높으면 스카우터들이 단점으로 지적하는 것으로 볼 때, 시스템적으로는 낮은 선수가 높은 평가를 받는다. 단, 비가 오는 경기에선 펀칭빈도가 높은 골키퍼를 사용하는 것이 더 효율적이다.\n
    (11) 페널티 박스 장악력(Command Of Area): 페널티 박스 장악력은 수비수와 협력해서 페널티 박스를 장악하는 골키퍼의 능력을 나타낸다. 이 등급이 높아서 박스 전체를 장악하는 골키퍼는 거의 본능적으로 날아오는 크로스를 비롯한 각종 상황에 대처한다. (이 때 공중 장악력이 높으면 도움이 된다) 하지만 이 등급이 높아도 골키퍼가 크로스를 잡으려 할 가능성만 오를 뿐, 잡아낸다는 보장은 없다.''')

sinbang = pd.read_csv("./useData/GK_kshi.csv")
st.dataframe(sinbang, hide_index = True, use_container_width=True)
#데이터 불러오기
raw_file = open("./useData/player_link_url.txt", "r")
raw_list = raw_file.read().split("\n")
st.download_button(label="Download rawdata",
        data=f"'{raw_list}'",
        file_name='raw_file.txt',
        mime='text/csv')

st.markdown(":floppy_disk: 선수 세부정보가 포함된 링크 크롤링 코드")
st.code('''
from bs4 import BeautifulSoup 
import requests

#라이브러리 호출
#라이브러리
from selenium import webdriver # Selenium의 웹 드라이버를 사용하기 위한 모듈을 임포트
from selenium.webdriver.common.by import By # Selenium에서 사용하는 By 클래스를 임포트합니다. 이 클래스는 웹 요소를 검색하는데 사용
from selenium.webdriver.common.keys import Keys #키보드 입력을 제어하기 위한 Keys 클래스를 임포트
from selenium.webdriver.chrome.service import Service # Chrome 드라이버 서비스를 사용하기 위한 모듈을 임포트
from selenium.webdriver.chrome.options import Options # Chrome 드라이버 옵션을 설정하기 위한 클래스를 임포트
from webdriver_manager.chrome import ChromeDriverManager #Chrome 드라이버를 자동으로 설치 및 관리하는 데 사용되는 매니저를 임포트
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time #시간 관련 함수를 사용하기 위한 time 모듈을 임포
        
#옵션객체 생성
sel_opt = Options() 
sel_opt.add_experimental_option("excludeSwitches", ["enable-automation"]) #드라이버 시작시 불필요문구 미표시되도록 설정
sel_opt.add_experimental_option("excludeSwitches", ["enable-logging"]) #터미널상의 불필요문구 미표시되도록 설정
# ma_option.add_argument("--headless") #드라이버창 안열리게 설정
sel_opt.add_argument("--start-maximized") # 화면크기 최대화
sel_opt.add_argument("--disable-gpu") #헤드리스가 안될경우 함께 사용
sel_opt.add_experimental_option("detach", True)  # 화면꺼짐 방지옵션 추가
sel_opt.add_argument("--incognito") #시크릿모드로 진행

#드라이버 세팅
srt_sevice = Service(ChromeDriverManager().install()) #드라이버설치
core_driver = webdriver.Chrome(service=srt_sevice, options=sel_opt)

#타겟링크 지정 정보수신
target_Url = "https://fminside.net/players#google_vignette"
core_driver.get(target_Url)
time.sleep(10)
        
# 무한 루프 시작
while True:
    try:
        # 'loadmore' 클래스를 가진 버튼 찾기
        more_btn = WebDriverWait(core_driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "loadmore")))
        # 버튼 클릭
        more_btn.click()
        # 3초 대기 (페이지 로드를 기다리기 위함)
        time.sleep(3)
    except TimeoutException:
        # 만약에 'loadmore' 버튼이 없으면 break로 탈출
        break
    except ElementClickInterceptedException:
        # 클릭할 수 없는 경우, 페이지가 로드될 때까지 대기 후 다시 시도
        time.sleep(3)

#전처리
raw_data = list()
player_href = core_driver.find_elements(By.TAG_NAME, "b") #태그네임이 b인 것을 리스트로 저장
for v in player_href: #반복문을 통해 b태그의 outerHTML 요소 값 추출 및 빈리스트에 추가
    raw = v.get_attribute("outerHTML")
    raw_data.append(raw)
#outerHTML 요소를 split 하여 링크 주소 추출 및 메인 도메인 주소와 합쳐 완성형 주소로 전처리
for v in raw_data:
    back_rul = v.split("href=")[1].split("'>'"''")[0]
    full_url = "https://fminside.net"+back_rul
    print(full_url)
''')

st.markdown(":floppy_disk: 선수 세부정보 크롤링 코드")
st.code('''
#라이브러리 호출
from bs4 import BeautifulSoup 
import pandas as pd
import requests
#데이터 불러오기
raw_file = open("./player_link_url.txt", "r")
raw_list = raw_file.read().split("\n")
print(len(raw_list))
# 선수별 세부링크 변수 
real_link = raw_list

# 데이터 프레임에 사용할 리스트
basic_field = ["player_nm", "player_overall", "player_potential", "player_team", "player_country", "player_position", "player_age", "player_foot", "player_height", "player_Weight"]
nonGK_field_nm = ['corners', 'crossing', 'dribbling', 'finishing', 'first-touch', 'free-kick-taking', 'heading', 'long-shots', 'long-throws', 'marking', 'passing', 'penalty-taking', 'tackling', 'technique', 'aggression', 'anticipation', 'bravery', 'composure', 'concentration', 'decisions', 'determination', 'flair', 'leadership', 'off-the-ball', 'positioning', 'teamwork', 'vision', 'work-rate', 'acceleration', 'agility', 'balance', 'jumping-reach', 'natural-fitness', 'pace', 'stamina', 'strength']
GK_field_nm = ['aerial-reach', 'command-of-area', 'communication', 'eccentricity', 'first-touch', 'handling', 'kicking', 'one-on-ones', 'passing', 'punching-tendency', 'reflexes', 'rushing-out-tendency', 'throwing', 'aggression', 'anticipation', 'bravery', 'composure', 'concentration', 'decisions', 'determination', 'flair', 'leadership', 'off-the-ball', 'positioning', 'teamwork', 'vision', 'work-rate', 'acceleration', 'agility', 'balance', 'jumping-reach', 'natural-fitness', 'pace', 'stamina', 'strength', 'free-kick-taking', 'penalty-taking', 'technique']

# 선수 정보를 저장할 데이터프레임 초기화
Basic_nongk_df = pd.DataFrame(columns=basic_field)
Basic_gk_df = pd.DataFrame(columns=basic_field)
nonGK_df = pd.DataFrame(columns=nonGK_field_nm)
GK_df = pd.DataFrame(columns=GK_field_nm)

# 뷰티풀숲을 통한 크롤링
now_num = 1
for link in real_link[:30]:
    print(now_num + real_link.index(link))
    get_info = requests.get(link)
    all_data = get_info.text
    myparser = BeautifulSoup(all_data, 'html.parser')  # 해당 링크 html 파싱

    # 프로필
    target_area = myparser.select("div#player_info")

    for lt in target_area:
        try:
            player_position = lt.select_one("div#player > div.title > div.meta > ul > li > span.value > span.desktop_positions").text
            player_nm = lt.select_one("div#player > div.title > h1").text
            player_overall = lt.select_one("div#player > div.title > div.meta > span#ability").text
            player_potential = lt.select_one("div#player > div.title > div.meta > span#potential").text
            player_team = lt.select_one("div#player > div.title > div.meta > ul > li > a > span.value").text
            player_country = lt.select_one("div#player > div.title > div.meta > ul > li > span.value > a").text

            # 좌측하단 선수 프로필
            for ld in target_area:
                player_column = ld.select("div#player > div.column > ul > li")
                for ld_v in player_column:
                    if ld_v.select_one("span.key").text == "Age":
                        player_age = ld_v.select_one("span.value").text
                    elif ld_v.select_one("span.key").text == "Foot":
                        player_foot = ld_v.select_one("span.value").text
                    elif ld_v.select_one("span.key").text == "Height":
                        player_Height = ld_v.select_one("span.value").text.split(" ")[0]
                    elif ld_v.select_one("span.key").text == "Weight":
                        player_Weight = ld_v.select_one("span.value").text.split(" ")[0]

            # 우측 프로필
            stat_columns = myparser.select("div#right_column > div.block.stats > div.column > table > tr > td[class^='stat value_']")
            stat_num = [vv.text for vv in stat_columns]

            
            # 세부 속성 데이터를 기존 데이터프레임에 추가
            if player_position != "GK" and len(stat_num) == len(nonGK_field_nm):
                nonGK_df.loc[len(nonGK_df)] = stat_num
                # 기본 속성 데이터를 기존 데이터프레임에 추가
                Basic_nongk_df.loc[len(Basic_nongk_df)] = [player_nm, player_overall, player_potential, player_team, player_country, player_position, player_age, player_foot, player_Height, player_Weight]
            elif player_position == "GK" and len(stat_num) == len(GK_field_nm):
                GK_df.loc[len(GK_df)] = stat_num
                # 기본 속성 데이터를 기존 데이터프레임에 추가
                Basic_gk_df.loc[len(Basic_gk_df)] = [player_nm, player_overall, player_potential, player_team, player_country, player_position, player_age, player_foot, player_Height, player_Weight]
            else:
                pass

        except AttributeError:
            player_team = "NaN"
            player_country = "NaN"
            player_position = "NaN"

# 데이터프레임 컨캣
final_player_GKdf = pd.concat([Basic_gk_df, GK_df], axis=1)
final_player_nonGKdf = pd.concat([Basic_nongk_df, nonGK_df], axis=1)
''')
st.markdown("------")

st.subheader(":two: 23/24년도 유럽 5 대 리그별 경기결과")
st.markdown(":white_check_mark:데이터 출처 : FotMob(https://www.fotmob.com/en-GB)")
st.markdown(":white_check_mark:데이터 소개 : 23년도, 24년도 유렵축구 5 대리그별 경기결과와 경기별 출전선수 라인업 정보가 포함되어있는 데이터")
st.markdown(":white_check_mark: 데이터 활용계획")
st.text("- 승부 예측(팀/포지션별 속성 수치 기반)\n- 랭체인기반 챗봇(선수정보 등)")
st.dataframe(pd.read_csv("./useData/match_result.csv"), hide_index = True, use_container_width=True)
st.markdown(":floppy_disk: 5대 리그별 경기결과 크롤링 코드")
st.code('''
import selenium
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
from selenium import webdriver #Selenium의 웹 드라이버를 사용하기 위한 모듈을 임포트
from selenium.webdriver.common.by import By #Selenium에서 사용하는 By 클래스를 임포트합. 웹 요소를 검색하는데 사용.
from selenium.webdriver.common.keys import Keys #키보드 입력 제어를 위해 Keys 클래스 임포트
from selenium.webdriver.chrome.service import Service #Chrome 드라이버 서비스를 사용하기 위한 모듈 임포트
from selenium.webdriver.chrome.options import Options #Chrome 드라이버 옵션을 설정하기 위한 클래스 임포트
from webdriver_manager.chrome import ChromeDriverManager #Chrome 드라이버를 자동으로 설치 및 관리하는데 사용되는 드라이버 매니저 임포트
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import requests

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
#불필요한 에러 메서지 없애기
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])

# 경기 정보 링크
# epl
epl_url='https://www.fotmob.com/en-GB/leagues/47/matches/premier-league/by-round'
driver = webdriver.Chrome(options=chrome_options)
driver.get(epl_url)
driver.maximize_window()
driver.implicitly_wait(5)
roundBtn=driver.find_elements(By.CSS_SELECTOR,'div>select')[1]
rounds=roundBtn.find_elements(By.TAG_NAME,'option')
matchLinkDict={'EPL':[]}
matchHrefs=[]
baseLink='https://www.fotmob.com'
for i in rounds:
    i.click()
    print(f'---Round {i.text} Start!---')
    time.sleep(1)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    matchContainer=soup.select('div.slick-slide.slick-active>div>section>a')
    for j in matchContainer:
        matchHrefs.append(j.get('href'))
    time.sleep(1)
driver.close()
matchLinkDict['EPL']=[i+j for i,j in zip([baseLink]*len(matchHrefs),matchHrefs)]
print('Match Link Parsing Done!')

#라리가
laliga_url='https://www.fotmob.com/en-GB/leagues/87/matches/laliga/by-round'
driver = webdriver.Chrome(options=chrome_options)
driver.get(laliga_url)
driver.maximize_window()
driver.implicitly_wait(5)
roundBtn=driver.find_elements(By.CSS_SELECTOR,'div>select')[1]
rounds=roundBtn.find_elements(By.TAG_NAME,'option')
matchLinkDict['LaLiga']=[]
matchHrefs=[]
baseLink='https://www.fotmob.com'
for i in rounds:
    i.click()
    print(f'---Round {i.text} Start!---')
    time.sleep(1)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    matchContainer=soup.select('div.slick-slide.slick-active>div>section>a')
    for j in matchContainer:
        matchHrefs.append(j.get('href'))
    time.sleep(1)
driver.close()
matchLinkDict['LaLiga']=[i+j for i,j in zip([baseLink]*len(matchHrefs),matchHrefs)]
print('Match Link Parsing Done!')

# 분데스리가
bundes_url='https://www.fotmob.com/en-GB/leagues/54/matches/bundesliga/by-round'
driver = webdriver.Chrome(options=chrome_options)
driver.get(bundes_url)
driver.maximize_window()
driver.implicitly_wait(5)
roundBtn=driver.find_elements(By.CSS_SELECTOR,'div>select')[1]
rounds=roundBtn.find_elements(By.TAG_NAME,'option')
matchLinkDict['Bundesliga']=[]
matchHrefs=[]
baseLink='https://www.fotmob.com'
for i in rounds:
    i.click()
    print(f'---Round {i.text} Start!---')
    time.sleep(1)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    matchContainer=soup.select('div.slick-slide.slick-active>div>section>a')
    for j in matchContainer:
        matchHrefs.append(j.get('href'))
    time.sleep(1)
driver.close()
matchLinkDict['Bundesliga']=[i+j for i,j in zip([baseLink]*len(matchHrefs),matchHrefs)]
print('Match Link Parsing Done!')

# 세리아
serieA_url='https://www.fotmob.com/en-GB/leagues/55/matches/serie/by-round'
driver = webdriver.Chrome(options=chrome_options)
driver.get(serieA_url)
driver.maximize_window()
driver.implicitly_wait(5)
roundBtn=driver.find_elements(By.CSS_SELECTOR,'div>select')[1]
rounds=roundBtn.find_elements(By.TAG_NAME,'option')
matchLinkDict['Serie-A']=[]
matchHrefs=[]
baseLink='https://www.fotmob.com'
for i in rounds:
    i.click()
    print(f'---Round {i.text} Start!---')
    time.sleep(1)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    matchContainer=soup.select('div.slick-slide.slick-active>div>section>a')
    for j in matchContainer:
        matchHrefs.append(j.get('href'))
    time.sleep(1)
driver.close()
matchLinkDict['Serie-A']=[i+j for i,j in zip([baseLink]*len(matchHrefs),matchHrefs)]
print('Match Link Parsing Done!')

# 리그앙
ligue1_url='https://www.fotmob.com/en-GB/leagues/53/matches/ligue-1/by-round'
driver = webdriver.Chrome(options=chrome_options)
driver.get(ligue1_url)
driver.maximize_window()
driver.implicitly_wait(5)
roundBtn=driver.find_elements(By.CSS_SELECTOR,'div>select')[1]
rounds=roundBtn.find_elements(By.TAG_NAME,'option')
matchLinkDict['Ligue-1']=[]
matchHrefs=[]
baseLink='https://www.fotmob.com'
for i in rounds:
    i.click()
    print(f'---Round {i.text} Start!---')
    time.sleep(1)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    matchContainer=soup.select('div.slick-slide.slick-active>div>section>a')
    for j in matchContainer:
        matchHrefs.append(j.get('href'))
    time.sleep(1)
driver.close()
matchLinkDict['Ligue-1']=[i+j for i,j in zip([baseLink]*len(matchHrefs),matchHrefs)]
print('Match Link Parsing Done!')

# 저장할 JSON 파일 경로
file_path = './data/match_link.json'

# 딕셔너리를 JSON 파일로 저장
with open(file_path, 'w') as json_file:
    json.dump(matchLinkDict, json_file)

# 페이지 파싱
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
matchResultSoupDict={}
for league in matchLinkDict.keys():
    key=league+'_result'
    matchResultSoupDict[key]=[]
    for i in matchLinkDict[league]:
        driver.get(i)
        try:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div>section.css-1jf4irq-ExpandableCardContainerStyle.e360fsv1')))
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            matchResultSoupDict[key].append(soup)
            print(f"{league} {matchLinkDict[league].index(i)+1}/{len(matchLinkDict[league])}")
        except:
            print(f"Pass {league} {matchLinkDict[league].index(i)+1}/{len(matchLinkDict[league])}")
            pass
print('Done!')
driver.close()

# 매치결과 데이터프레임으로 변환
matchResultDf=pd.DataFrame()
for i in matchResultSoupDict.keys():
    leagueName=i.split('_')[0]
    for j in matchResultSoupDict[i]:
        # 매치 결과 요약 컨테이너
        matchResultContainer=j.select_one('div>section>header.css-1dpguef-MFHeaderFullscreenHeader.e3q4wbq3')
        # 홈팀 이름
        homeTeam=matchResultContainer.select(
            'span>span.css-1ba2www-TeamNameItself-TeamNameOnTabletUp-hideOnMobile.e1rexsj40')[0].text
        # 어위이팀 이름
        awayTeam=matchResultContainer.select(
            'span>span.css-1ba2www-TeamNameItself-TeamNameOnTabletUp-hideOnMobile.e1rexsj40')[1].text
        # 홈팀 득정
        homeScore=matchResultContainer.select_one(
            'div.css-1cf82ng-MFHeaderStatusWrapper.ed9bevl13').text[:5].split(' ')[0]
        # 어위이팀 득점
        awayScore=matchResultContainer.select_one(
            'div.css-1cf82ng-MFHeaderStatusWrapper.ed9bevl13').text[:5].split(' ')[-1]
        # Home : 홈팀 승리, Draw : 동점, Away : 어웨이팀 승리
        if homeScore>awayScore:
            matchResult='Home'
        elif homeScore==awayScore:
            matchResult='Draw'
        else:
            matchResult='Away'
        tempDf=pd.DataFrame({
            'league':leagueName,
            'homeTeam':[homeTeam],
            'awayTeam':[awayTeam],
            'homeScore':[homeScore],
            'awayScore':[awayScore],
            'matchResult':[matchResult]
        })
        matchResultDf=pd.concat([matchResultDf,tempDf])
matchResultDf=matchResultDf.reset_index().drop('index',axis=1)

# 리그 소속국가 추가
nationLeagueMappingDict={}
for i,j in zip(list(matchResultDf['league'].unique()),['England','Germany','Italy','France','Spain']):
    nationLeagueMappingDict[i]=j
leagueNation=[nationLeagueMappingDict[i] for i in matchResultDf['league']]
matchResultDf.insert(0,'leagueNation',leagueNation)
matchResultDf.to_csv(./data/match_result.csv')
''')

st.markdown("-----")
st.subheader(":three: 24년도 유럽축구리그별 1, 2부 선수 Market-Value")
st.markdown(":white_check_mark:데이터 출처 : Transform markt(https://www.transfermarkt.com/)")
st.markdown(":white_check_mark:데이터 소개 : 24년도 유렵축구 5대리그의 1,2부 선수 몸값 정보가 포함된 데이터")
st.markdown(":white_check_mark: 데이터 활용계획")
st.text("- 포지션별 유사선수 클러스터링\n- 선수 몸값 예측\n- 랭체인기반 챗봇(선수정보 등)")

tab1, tab2, tab3, tab4, tab5 = st.tabs(['England', 'Germany', 'Spain', 'Italy', 'France'])

with tab1:
    eng_player = pd.read_csv("./useData/transfermarket_englandtotal.csv")
    st.dataframe(eng_player, use_container_width=True, hide_index=True)

with tab2:
    ger_player = pd.read_csv("./useData/transfermarket_germanytotal.csv")
    st.dataframe(ger_player, use_container_width=True, hide_index=True)

with tab3:
    spain_player = pd.read_csv("./useData/transfermarket_spaintotal.csv")
    st.dataframe(spain_player, use_container_width=True, hide_index=True)

with tab4:
    italy_player = pd.read_csv("./useData/transfermarket_italytotal.csv")
    st.dataframe(italy_player, use_container_width=True, hide_index=True)

with tab5:
    france_player = pd.read_csv("./useData/transfermarket_francetotal.csv")
    st.dataframe(france_player, use_container_width=True, hide_index=True)   


st.markdown("-----")
st.subheader(":four: Foot-Ball RSS(Rich Site Summary)")
st.markdown(":white_check_mark:데이터 출처")
st.text("- BBC Sports(영국 링크) : https://www.bbc.com/sport/football\n- Kicker(독일 링크) : http://www.kicker.de/\n- ABC Deportes(스페인 링크) : http://www.abc.es/deportes/futbol-formula1-tenis.asp\n- Gianluca Dimarzio(이탈리아 링크) : http://gianlucadimarzio.com/")
st.markdown(":white_check_mark: 데이터 활용계획")
st.text("주기별로 해외 4개국 주요 축구뉴스 사이트에서 수집한 데이터를 활용해 Lang-Chain 기반의 자동번역/요약을 통한 정보제공")
st.image("./useData/news.png")
