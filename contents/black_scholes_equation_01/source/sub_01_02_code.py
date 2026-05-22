from manim import *
import itertools

class PermutationStepByStep(Scene):
    def construct(self):

        # 1. 데이터 준비
        characters = "ABCD"
        perms = list(itertools.permutations(characters))
        
        # 전체 그룹 생성
        perm_group = VGroup()
        for p in perms:
            text_str = "".join(p)
            text_mobject = Text(text_str, font_size=30)
            perm_group.add(text_mobject)
            
        # 배치: 6행 4열 (세로로 길게 배치해야 흐름이 잘 보임)
        # 행: 24개, 열: 1개로 처리하거나 grid로 배치
        # 설명의 편의를 위해 6개씩 4개의 덩어리로 묶어서 가로로 배치
        # Column 1: A..., Column 2: B..., Column 3: C..., Column 4: D...
        perm_group.arrange_in_grid(rows=6, cols=4, buff=0.5, flow_order="dr")
        
        # 그리드 배치 후 오른쪽으로 이동
        perm_group.to_edge(RIGHT, buff=1.0) 

        self.play(Write(perm_group), run_time=3)
        self.wait()

        # ---------------------------------------------------------
        # 1. 왼쪽: 밑줄(Slot) 4개 생성
        # ---------------------------------------------------------
        # 밑줄 4개를 담을 그룹
        slots = VGroup()
        for i in range(4):
            # 밑줄 하나 생성 (Line 객체)
            line = Line(start=LEFT, end=RIGHT).set_width(0.5)
            slots.add(line)
            
        # 밑줄들을 가로로 배치
        slots.arrange(RIGHT, buff=0.5)
        
        # 화면의 왼쪽(-4, 0, 0) 정도 위치로 이동
        slots.to_edge(LEFT, buff=1.0) 
        
        self.play(Write(slots))

        # 슬롯 선택 예제
        # self.play(slots[1].animate.set_color(RED))


        # ---------------------------------------------------------
        # Step 1: 첫 번째 자리는 A, B, C, D 모두 올 수 있다.
        # ---------------------------------------------------------
        
        # 각 열(Column)의 첫 글자들만 강조하기 위해 인덱싱
        # perms 리스트 순서와 grid 배치가 col_major이므로
        # 0~5번: A시작, 6~11번: B시작, 12~17번: C시작, 18~23번: D시작
        
        # 첫 글자들만 수집
        first_chars = VGroup()
        for item in perm_group:
            first_chars.add(item[0]) # 각 텍스트의 첫 글자

        # 첫글자 노란색으로 강조
        self.play(
            first_chars.animate.set_color(YELLOW),
            run_time=2
        )
        self.wait(1)
        
        # 첫글자 하나씩 uniqe에 담기
        first_chars_uniqe = VGroup()
        for i in range(0, len(first_chars), 6):
            first_chars_uniqe.add(first_chars[i].copy())
        
        # uniqe를 의자 밑에 나열
        first_chars_uniqe.arrange(DOWN, buff=0.2).next_to(slots[0], DOWN, buff=0.5)

        j=0
        for i in range(len(first_chars_uniqe)):
            self.play(
                Transform(first_chars[j:j+6].copy(), first_chars_uniqe[i])
            )
            j += 6
            self.wait(0.5)



        # self.play(
        #     first_chars_uniqe.animate.next_to(slots[0], DOWN, buff=0.5)
        # )
        # self.wait(1)

        # 의자 위에 ABCD를 위치시킴
        first_chars_uniqe_copy = VGroup(*first_chars_uniqe.copy())

        for i in range(len(first_chars_uniqe_copy)):
            first_chars_uniqe_copy[i].next_to(slots[i], UP, buff=0.2).scale(1.5).set_color(RED)


        # A를 자리에 앉힘
        self.play(
            Transform(first_chars_uniqe[0], first_chars_uniqe_copy[0])
        )


        # "첫 번째 자리에 A를 선택한다" -> A로 시작하는 첫 번째 열만 남기고 나머지 흐리게 처리
        col_A = perm_group[:6]      # A로 시작하는 6개
        others = perm_group[6:]     # B, C, D로 시작하는 나머지
        
        # 핵심: col_A 내부에서 첫 글자를 제외한 "나머지 뒷부분(BCD...)"만 수집
        # item[1:] -> 1번 인덱스부터 끝까지 (즉, 첫 글자 제외)
        col_A_rest = VGroup(*[item[1:] for item in col_A])



        # self.play(
        #     others.animate.set_opacity(0.2), # 나머지는 흐리게
        #     # first_chars.animate.set_color(WHITE).set_opacity(0.2), # 강조 원복
        #     run_time=2
        # )
        
        # A 그룹의 첫 글자(A)만 빨간색으로 확정 표시
        first_A_chars = VGroup(*[item[0] for item in col_A])
        self.play(
            first_A_chars.animate.set_color(RED),
            others.animate.set_opacity(0.2)
        )
        self.wait(1)

        # ---------------------------------------------------------
        # Step 2: A를 선택했으니, 두 번째 자리는 B, C, D가 올 수 있다.
        # ---------------------------------------------------------
        
        # A 그룹(6개) 내에서 두 번째 글자들 수집
        second_chars_in_A = VGroup(*[item[1] for item in col_A])
        
        self.play(
            second_chars_in_A.animate.set_color(YELLOW),
            run_time=2
        )
        self.wait(1)
        
        first_chars_uniqe3 = VGroup(*first_chars_uniqe[1:])

 
        # 두 번째 글자들을 의자 밑에 나열
        first_chars_uniqe3.arrange(DOWN, buff=0.2).next_to(slots[1], DOWN, buff=0.5)

        j=0
        for i in range(len(first_chars_uniqe[1:])):
            self.play(
                Transform(second_chars_in_A[j:j+2].copy(), first_chars_uniqe3[i])
            )
            j += 2
            self.wait(0.5)


        # B를 자리에 앉힘
        self.play(
            Transform(first_chars_uniqe[1], first_chars_uniqe_copy[1])
        )
        self.wait(1)


        # "두 번째 자리에 B를 선택한다" -> A 그룹 안에서도 B가 두 번째인 것(AB..)만 선택
        # A로 시작하는 6개 중: AB.., AB.., AC.., AC.., AD.., AD.. 순서임
        # 즉 처음 2개가 AB로 시작함
        sub_AB = col_A[:2]     # AB.. (2개)
        sub_others = col_A[2:] # AC.., AD.. (나머지 4개)
        
        # self.play(
        #     sub_others.animate.set_opacity(0.2), # A그룹 내의 탈락자들 흐리게
        #     # second_chars_in_A.animate.set_color(WHITE).set_opacity(0.2), # 강조 원복
        #     run_time=2
        # )
        
        # AB 그룹의 두 번째 글자(B)만 빨간색으로 확정 표시
        second_B_chars = VGroup(*[item[1] for item in sub_AB])
        self.play(
            second_B_chars.animate.set_color(RED),
            sub_others.animate.set_opacity(0.2)
        )
        self.wait(1)




        # ---------------------------------------------------------
        # Step 3: A, B를 선택했으니, 세 번째 자리는 C, D가 올 수 있다.
        # ---------------------------------------------------------
        
        # AB 그룹(2개) 내에서 세 번째 글자들 수집
        third_chars_in_AB = VGroup(*[item[2] for item in sub_AB])
        
        self.play(
            third_chars_in_AB.animate.set_color(YELLOW),
            run_time=2
        )
        self.wait(1)




        first_chars_uniqe2 = VGroup(*first_chars_uniqe[2:])

 
        # 세 번째 글자들을 의자 밑에 나열
        first_chars_uniqe2.arrange(DOWN, buff=0.2).next_to(slots[2], DOWN, buff=0.5)

        for i in range(len(first_chars_uniqe[2:])):
            self.play(
                Transform(third_chars_in_AB[i].copy(), first_chars_uniqe2[i])
            )
            self.wait(0.5)


        # c를 자리에 앉힘
        self.play(
            Transform(first_chars_uniqe2[0].copy(), first_chars_uniqe_copy[2])
        )
        self.wait(1)

# region

        # "세 번째 자리에 C를 선택한다" -> ABC.. 만 남김
        # sub_AB[0]은 ABCD, sub_AB[1]은 ABDC
        target_ABC = sub_AB[0]
        target_ABD = sub_AB[1]
        
        self.play(
            target_ABD.animate.set_opacity(0.2),
            target_ABC[2].animate.set_color(RED), # C를 빨간색으로
            run_time=2
        )
        self.wait(1)

        target_ABCD = VGroup(*target_ABC.copy())


        # 네 번째 글자들을 의자 밑에 나열
        target_ABCD[3].arrange(DOWN, buff=0.2).next_to(slots[3], DOWN, buff=0.5).set_color(YELLOW)

        self.play(
            Transform(target_ABC[3].copy(), target_ABCD[3])
        )


        # D를 의자에 앉힘
        self.play(
            Transform(target_ABCD[3].copy(), first_chars_uniqe_copy[3]),
            target_ABC[3].animate.set_color(RED), # D를 빨간색으로
        )
        self.wait(1)       

#endregion



        # 숫자 4, 3, 2, 1을 배치할 그룹 생성
        count_numbers = VGroup()
        
        # 4, 3, 2, 1 순서로 텍스트 생성 및 배치
        for i, num in enumerate([4, 3, 2, 1]):
            num_text = Text(str(num), font_size=40, color=YELLOW)
            num_text.next_to(first_chars_uniqe_copy[i], UP, buff=0.5)
            count_numbers.add(num_text)
            
        self.play(Write(count_numbers),
            run_time=3
        )


        # 43
        self.play(
            perm_group.animate.set_opacity(1.0),
            run_time=1
        )



        # perm_group 왼쪽에 6, 상단에 4 브라켓 추가
        brace_left = Brace(perm_group, direction=LEFT)
        label_6 = Text("6", font_size=40).next_to(brace_left, LEFT)
        
        brace_top = Brace(perm_group, direction=UP)
        label_4 = Text("4", font_size=40).next_to(brace_top, UP)
        
        self.play(
            LaggedStart(Create(brace_left), Write(label_6), lag_ratio=0.5),
            run_time=2
        )
        self.wait()

        self.play(
            LaggedStart(Create(brace_top), Write(label_4), lag_ratio=0.5),
            run_time=2
        )



        self.play(
            Wiggle(first_chars[0], scale_value=1.3, rotation_angle=0.03*TAU),
            Wiggle(first_chars[6], scale_value=1.3, rotation_angle=0.03*TAU),
            Wiggle(first_chars[12], scale_value=1.3, rotation_angle=0.03*TAU),
            Wiggle(first_chars[18], scale_value=1.3, rotation_angle=0.03*TAU),
        )

            

        # 이동 애니메이션을 위한 리스트 준비
        anims = []
        j = 0
        for i in range(len(first_chars_uniqe)):
            # 복사본 생성 및 화면에 추가
            moving_char = first_chars[j].copy()
            self.add(moving_char)
            
            # 애니메이션 정의 (이동)
            anims.append(moving_char.animate.move_to(count_numbers[0]))
            j += 6
            
        # LaggedStart를 사용하여 겹쳐서 빠르게 실행
        self.play(
            LaggedStart(*anims, lag_ratio=1),
            remover=True, # 애니메이션 후 객체 제거
            run_time=3,  # 전체 실행 시간
            # rate_func=rate_functions.ease_in_quad # 점점 빨리 날아가도록 가속
        )

        self.wait()


        # col_A(A로 시작하는 6개)를 2개씩 묶어서 순서대로 박스 치기
        rects = VGroup()
        # 0, 2, 4 인덱스로 시작하여 2개씩 묶음
        for i in range(0, len(col_A), 2):
            group_2 = col_A[i:i+2]
            rect = SurroundingRectangle(group_2, color=BLUE, buff=0.1)
            rects.add(rect)
            
        self.play(
            LaggedStart(*[Create(rect) for rect in rects], lag_ratio=0.5),
            run_time=2
        )
        self.wait()

        twotwo = MathTex(r"2 + 2 + 2")

        twotwo.next_to(label_6, DL).shift(RIGHT*0.8)

        self.play(
            LaggedStart(
                ReplacementTransform(rects[0], twotwo[0][0]),
                ReplacementTransform(rects[1], twotwo[0][2]),
                ReplacementTransform(rects[2], twotwo[0][4]), 
                lag_ratio=0.5
            )
        )

        self.play(
            Write(twotwo[0][1]),
            Write(twotwo[0][3]),
        )


        threetwo = MathTex(r"2 \times 3")
        threetwo.next_to(twotwo, DOWN, buff=0.3)

         # 2 \times만 먼저 보이기
        self.play(
            twotwo[0][0].copy().animate.move_to(threetwo[0][0])
        )
        self.wait(0.5)

        # + 기호는 사라짐
        self.play(
                Transform(twotwo[0][1].copy(), threetwo[0][1]),
                Transform(twotwo[0][3].copy(), threetwo[0][1]),
        )
        self.wait(0.5)

        num_one = MathTex(r"1")
        num_two = MathTex(r"2")
        num_three = MathTex(r"3")
        nums = VGroup(num_one, num_two, num_three)
        nums.move_to(threetwo[0][2])



        # 숫자 2가 하나씩 내려오면서 3의 위치로 이동
        c1 = twotwo[0][0].copy()
        c2 = twotwo[0][2].copy()
        c3 = twotwo[0][4].copy()

        # 1. 첫 번째 2 이동 후 1이 됨
        self.play(c1.animate.move_to(threetwo[0][2]), run_time=0.5)
        self.play(
            FadeIn(nums[0][0]),
            FadeOut(c1),
            run_time=0.2
        )

        # 2. 두 번째 2 이동 후 1이 2가 됨
        self.play(c2.animate.move_to(threetwo[0][2]), run_time=0.5)
        self.play(
            ReplacementTransform(nums[0][0], nums[1][0]),
            FadeOut(c2),
            run_time=0.2
        )

        # 3. 세 번째 2 이동 후 2가 3이 됨
        self.play(c3.animate.move_to(threetwo[0][2]), run_time=0.5)
        self.play(
            ReplacementTransform(nums[1][0], threetwo[0][2]),
            FadeOut(c3),
            run_time=0.2
        )
        self.wait()


        self.play(
            perm_group.animate.set_opacity(0.2),
            run_time=0.5
        )


        group_count = MathTex(r"4 \times 6 = 24")
        group_count.scale(1.5)
        group_count.move_to(perm_group)
        
        label_6_copy = label_6.copy()
        label_4_copy = label_4.copy()

        self.play(
            LaggedStart(
                label_4_copy.animate.move_to(group_count[0][0]).scale(1.5),
                Write(group_count[0][1]),
                label_6_copy.animate.move_to(group_count[0][2]).scale(1.5),
                Write(group_count[0][3:]), 
                lag_ratio=1
            )
        )
        self.wait()


        # 6을 3 \times 2로 바꾸기
        final_eq = MathTex(r"4 \times 3 \times 2 = 24")
        final_eq.scale(1.5)
        final_eq.move_to(group_count)

        threetwo_copy = threetwo.copy()

        self.play(
            threetwo_copy.animate.move_to(group_count[0][2]).scale(1.5),
            run_time=1
        )
        self.remove(label_6_copy)

        self.play(
            ReplacementTransform(label_4_copy, final_eq[0][0]),
            ReplacementTransform(group_count[0][1], final_eq[0][1]),
            ReplacementTransform(threetwo_copy, final_eq[0][2:5]),
            ReplacementTransform(group_count[0][3:], final_eq[0][5:]),
        )
        self.wait()


        final_eq_seat = VGroup(Text(r"4 × 3 × 2 × 1 = 24", font_size=40, color=YELLOW))
        
        final_eq_seat.move_to(count_numbers.get_left(), aligned_edge=LEFT)



        self.play(
            ReplacementTransform(count_numbers[0], final_eq_seat[0][0]),
            Write(final_eq_seat[0][1]),
            ReplacementTransform(count_numbers[1], final_eq_seat[0][2]),
            Write(final_eq_seat[0][3]),
            ReplacementTransform(count_numbers[2], final_eq_seat[0][4]),
            Write(final_eq_seat[0][5]),
            ReplacementTransform(count_numbers[3], final_eq_seat[0][6]),
            Write(final_eq_seat[0][7:]),
            run_time=2
        )
        self.wait()



        self.play(
            Create(SurroundingRectangle(final_eq_seat[0][8:], color=RED, buff=0.1))
        )
        self.play(
            Create(SurroundingRectangle(final_eq[0][6:], color=RED, buff=0.1))
        )        

        self.play(
            Wiggle(final_eq_seat[0][8:], scale_value=1.3, rotation_angle=0.03*TAU),
            Wiggle(final_eq[0][6:], scale_value=1.3, rotation_angle=0.03*TAU)
        )        


        fourfac = Text(r"= 4!", font_size=40, color=YELLOW)
        fourfac.next_to(final_eq_seat, RIGHT)

        self.play(
            Write(fourfac)
        )

        self.wait(3)

        nfac = Text(r"= n!", font_size=40, color=YELLOW)
        nfac.next_to(fourfac, UP)    

        self.play(
            Write(nfac)
        )    

        self.wait(3)


# manim permutations5.py PermutationStepByStep -pql -n 74
