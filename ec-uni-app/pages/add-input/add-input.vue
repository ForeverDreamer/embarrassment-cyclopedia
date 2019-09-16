<template>
	<view>
		<!-- 自定义导航栏 -->
		<uni-nav-bar status-bar="true" right-text="发布" left-icon="arrowleft" @click-left="back" @click-right="submit" >
			<view class="u-f-ajc" @tap="changeLook">
				<view>所有人可见</view>
				<view class="icon iconfont icon-xialazhankai"></view>
			</view>
		</uni-nav-bar>
	</view>
</template>

<script>
	import uniNavBar from "../../components/uni-nav-bar/uni-nav-bar.vue"
	
	let chgLook = ['所有人可见', '仅自己可见'];
	
	export default {
		components: {
			uniNavBar
		},
		data() {
			return {
				yinsi: "所有人可见"
			}
		},
		methods: {
			// 返回
			back() {
				uni.navigateBack({
					delta: 1
				});
			},
			// 发布
			submit() {
				console.log("发布")
			},
			// 隐私
			changeLook() {
				uni.showActionSheet({
				    itemList: chgLook,
				    success: (res) => {
						console.log(res.tapIndex);
				        this.yinsi = chgLook[res.tapIndex];
				    }
				});
			}
		}
	}
</script>

<style>

</style>
